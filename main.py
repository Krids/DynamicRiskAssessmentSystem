"""
This file is responsible for the execution of this script.

Name: Felipe Lana Machado
Date: 30/08/2022
"""

import os
import sys
import logging as log
from argparse import ArgumentParser, Namespace
from src.pipeline.ingestion import IngestionPipeline

from src.utils.timer import Timer

PIPELINES = {
    "ingestion": IngestionPipeline(),
    # "training": TrainingPipeline(),
    # "diagnostics": DiagnosticsPipeline(),
    # "reporting": ReportingPipeline(),
    # "automation": AutomationPipeline(),
}

def get_args() -> Namespace:
    parser = ArgumentParser(description="Data Science Illuvium Modules")

    parser.add_argument(
        "--pipeline",
        "-p",
        type=str,
        required=False,
        choices=PIPELINES.keys(),
        help="Pipeline Name",
    )

    return parser.parse_args()

def main(args):
    
    log.basicConfig(
        level=log.INFO,
        filemode='w',
        format='%(name)s - %(levelname)s - %(message)s')
    timer = Timer()

    log.info(f"[APP] Args: {args}")

    pipeline = PIPELINES.get(args.pipeline.lower().strip(), None)
    if not pipeline:
        raise RuntimeError(f'Pipeline "{args.pipeline}" does not exist!')

    pipeline.run()

    log.info(f"[APP] Elapsed Time: {timer.stop()}")


if __name__ == '__main__':
    main(get_args())