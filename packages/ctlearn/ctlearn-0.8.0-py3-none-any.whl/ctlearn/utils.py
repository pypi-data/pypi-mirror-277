import importlib
import logging
import os
import pkg_resources
import sys
import time

import numpy as np
import pandas as pd
import tables
import yaml


def setup_logging(config, log_dir, debug, log_to_file):
    # Log configuration to a text file in the log dir
    time_str = time.strftime("%Y%m%d_%H%M%S")
    config_filename = os.path.join(log_dir, time_str + "_config.yml")
    with open(config_filename, "w") as outfile:
        ctlearn_version = pkg_resources.get_distribution("ctlearn").version
        tensorflow_version = pkg_resources.get_distribution("tensorflow").version
        outfile.write(
            "# Training performed with "
            "CTLearn version {} and TensorFlow version {}.\n".format(
                ctlearn_version, tensorflow_version
            )
        )
        yaml.dump(config, outfile, default_flow_style=False)

    # Set up logger
    logger = logging.getLogger()

    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    logger.handlers = []  # remove existing handlers from any previous runs
    if not log_to_file:
        handler = logging.StreamHandler()
    else:
        logging_filename = os.path.join(log_dir, time_str + "_logfile.log")
        handler = logging.FileHandler(logging_filename)
    handler.setFormatter(logging.Formatter("%(levelname)s:%(message)s"))
    logger.addHandler(handler)

    return logger


def setup_DL1DataReader(config, mode):
    # Parse file list or prediction file list
    if mode in ["train", "load_only"]:
        if isinstance(config["Data"]["file_list"], str):
            data_files = []
            with open(config["Data"]["file_list"]) as f:
                for line in f:
                    line = line.strip()
                    if line and line[0] != "#":
                        data_files.append(line)
            config["Data"]["file_list"] = data_files
        if not isinstance(config["Data"]["file_list"], list):
            raise ValueError(
                "Invalid file list '{}'. "
                "Must be list or path to file or directory".format(
                    config["Data"]["file_list"]
                )
            )
    else:
        file_list = config["Prediction"]["prediction_file_lists"][
            config["Prediction"]["prediction_file"]
        ]
        if file_list.endswith(".txt"):
            data_files = []
            with open(file_list) as f:
                for line in f:
                    line = line.strip()
                    if line and line[0] != "#":
                        data_files.append(line)
            config["Data"]["file_list"] = data_files
        elif file_list.endswith(".h5"):
            config["Data"]["file_list"] = [file_list]

        if os.path.isdir(file_list):
            config["Data"]["file_list"] = np.sort(
                np.array([file_list+x for x in os.listdir(file_list) if x.endswith(".h5")])
            ).tolist()

        if not isinstance(config["Data"]["file_list"], list):
            raise ValueError(
                "Invalid prediction file list '{}'. "
                "Must be list or path to file or directory".format(file_list)
            )

    mc_file = True
    dl1bparameter_names = None
    with tables.open_file(config["Data"]["file_list"][0], mode="r") as f:
        # Retrieve the data format of the hdf5 file
        if "CTA PRODUCT DATA MODEL NAME" in f.root._v_attrs:
            data_format = "stage1"
        elif "dl1_data_handler_version" in f.root._v_attrs:
            data_format = "dl1dh"
        else:
            raise ValueError(
                "Data format is not implemented in the DL1DH reader. Available data formats are 'stage1' and 'dl1dh'."
            )
        # Check weather the file is MC simulation or real observational data
        if data_format == "dl1dh" and "source_name" in f.root._v_attrs:
            mc_file = False
        # Retrieve the name convention for the dl1b parameters
        if data_format == "dl1dh":
            first_tablename = next(f.root.Parameters0._f_iter_nodes()).name
            dl1bparameter_names = f.root.Parameters0._f_get_child(f"{first_tablename}").colnames
        else:
            first_tablename = next(f.root.dl1.event.telescope.parameters._f_iter_nodes()).name
            dl1bparameter_names = f.root.dl1.event.telescope.parameters._f_get_child(f"{first_tablename}").colnames

    allow_overwrite = config["Data"].get("allow_overwrite", True)
    if "allow_overwrite" in config["Data"]:
        del config["Data"]["allow_overwrite"]

    selected_telescope_types = config["Data"]["selected_telescope_types"]
    camera_types = [tel_type.split("_")[-1] for tel_type in selected_telescope_types]

    tasks = config["Reco"]
    transformations = []
    event_info = []
    if data_format == "dl1dh":
        if "parameter_list" not in config["Data"] and dl1bparameter_names is not None and mode == "predict":
            config["Data"]["parameter_list"] = dl1bparameter_names
        # Parse list of event selection filters
        event_selection = {}
        for s in config["Data"].get("event_selection", {}):
            s = {"module": "dl1_data_handler.filters", **s}
            filter_fn, filter_params = load_from_module(**s)
            event_selection[filter_fn] = filter_params
        config["Data"]["event_selection"] = event_selection

        # Parse list of image selection filters
        image_selection = {}
        for s in config["Data"].get("image_selection", {}):
            s = {"module": "dl1_data_handler.filters", **s}
            filter_fn, filter_params = load_from_module(**s)
            image_selection[filter_fn] = filter_params
        config["Data"]["image_selection"] = image_selection

        if "direction" in tasks:
            event_info.append("src_pos_cam_x")
            event_info.append("src_pos_cam_y")
            transformations.append(
                {
                    "name": "AltAz",
                    "args": {
                        "alt_col_name": "src_pos_cam_x",
                        "az_col_name": "src_pos_cam_y",
                        "deg2rad": False,
                    },
                }
            )
    else:
        if "parameter_list" not in config["Data"] and dl1bparameter_names is not None and mode == "predict":
            config["Data"]["parameter_list"] = dl1bparameter_names
        if "direction" in tasks:
            event_info.append("true_alt")
            event_info.append("true_az")
            transformations.append({"name": "DeltaAltAz_fix_subarray"})

    if "particletype" in tasks:
        event_info.append("true_shower_primary_id")

    if "energy" in tasks:
        if mc_file:
            event_info.append("true_energy")
        transformations.append({"name": "MCEnergy"})

    concat_telescopes = config["Input"].get("concat_telescopes", False)
    if config["Data"]["mode"] == "stereo" and not concat_telescopes:
        for tel_desc in selected_telescope_types:
            transformations.append(
                {
                    "name": "SortTelescopes",
                    "args": {"sorting": "size", "tel_desc": f"{tel_desc}"},
                }
            )

    # Convert interpolation image shapes from lists to tuples, if present
    if "interpolation_image_shape" in config["Data"].get("mapping_settings", {}):
        config["Data"]["mapping_settings"]["interpolation_image_shape"] = {
            k: tuple(l)
            for k, l in config["Data"]["mapping_settings"][
                "interpolation_image_shape"
            ].items()
        }

    if allow_overwrite:
        config["Data"]["event_info"] = event_info
        config["Data"]["mapping_settings"]["camera_types"] = camera_types
    else:
        transformations = config["Data"].get("transforms", {})

    transforms = []
    # Parse list of Transforms
    for t in transformations:
        t = {"module": "dl1_data_handler.transforms", **t}
        transform, args = load_from_module(**t)
        transforms.append(transform(**args))
    config["Data"]["transforms"] = transforms

    # Possibly add additional info to load if predicting to write later
    if mode == "predict":
        if "Prediction" not in config:
            config["Prediction"] = {}
        if "event_info" not in config["Data"]:
            config["Data"]["event_info"] = []
        config["Data"]["event_info"].extend(["event_id", "obs_id"])
        if data_format == "dl1dh" and not mc_file:
            config["Data"]["event_info"].extend(["mjd", "milli_sec", "nano_sec"])

    return config["Data"], data_format


def load_from_module(name, module, path=None, args=None):
    if path is not None and path not in sys.path:
        sys.path.append(path)
    mod = importlib.import_module(module)
    fn = getattr(mod, name)
    params = args if args is not None else {}
    return fn, params
