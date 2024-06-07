"""Command line module for soil moisture prediction."""

import argparse
import json
import logging
import os
import time

from pydantic import ValidationError

from soil_moisture_prediction.pydantic_models import InputParamaters
from soil_moisture_prediction.random_forest_model import RFoModel

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--work_dir", type=str, required=True)
parser.add_argument(
    "-v",
    "--verbosity",
    choices=["quiet", "verbose", "debug"],
    default="verbose",
    help="Verbosity level (quiet, verbose [default], debug)",
)


def main(verbosity=None, work_dir=None):
    """Run the soil moisture prediction module."""
    if verbosity is None or work_dir is None:
        args = parser.parse_args()
        verbosity = args.verbosity
        work_dir = args.work_dir

    # Convert string choice to corresponding numeric level
    verbosity_levels = {"quiet": 30, "verbose": 20, "debug": 10}
    selected_verbosity = verbosity_levels[verbosity]

    logging.basicConfig(format="%(asctime)s - %(message)s", level=selected_verbosity)
    try:
        with open(os.path.join(work_dir, "parameters.json"), "r") as f_handle:
            input_parameters = InputParamaters(**json.loads(f_handle.read()))
    except ValidationError as e:
        logging.error("Invalid input parameters")
        for error in e.errors():
            logging.error(f"The field {error['loc'][0]} has an invalid value:")
            logging.error(f"{error['msg']}: {error['loc'][1]}")
        return None

    logging.debug("Input parameters:")
    logging.debug(json.dumps(input_parameters.model_dump(), indent=4))

    start_time = time.time()
    rfo_model = RFoModel(input_parameters=input_parameters, work_dir=work_dir)
    rfo_model.compute()
    rfo_model.plot_figure_selection()
    end_time = time.time()
    execution_time = end_time - start_time
    logging.info("Execution time: %.2f seconds", execution_time)

    return rfo_model


if __name__ == "__main__":
    main()
