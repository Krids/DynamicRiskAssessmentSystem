"""
This file is responsible for the execution of this script.

Name: Felipe Lana Machado
Date: 30/08/2022
"""

import logging as log
from argparse import ArgumentParser, Namespace
from src.pipeline.diagnostics import DiagnosticsPipeline
from src.api.app import ApiPipeline
from src.pipeline.fullprocess import FullprocessPipelie
from src.pipeline.ingestion import IngestionPipeline
from src.pipeline.reporting import ReportingPipeline
from src.pipeline.training_pipeline import TrainingPipeline

from src.utils.timer import Timer

PIPELINES = {
    "ingestion": IngestionPipeline(),
    "training": TrainingPipeline(),
    "diagnostics": DiagnosticsPipeline(),
    "reporting": ReportingPipeline(),
    "automation": FullprocessPipelie(),
    "api": ApiPipeline(),
}


def get_args() -> Namespace:
    parser = ArgumentParser(description="A Dynamic Risk Assessment System")

    parser.add_argument(
        "--pipeline",
        "-p",
        type=str,
        required=True,
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
