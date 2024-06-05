import argparse

from config import MerciExperimentConfig

import merci


def parse_args() -> MerciExperimentConfig:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--evaluator_type",
        type=merci.ModelEvaluator,
        default=merci.evaluate.DistributionShiftEvaluator,
    )
    parser.add_argument("--train_to_test_ratio", type=float, default=0.8)
    parser.add_argument("--output_path", type=str, default="output")

    args = parser.parse_args()
    cfg = MerciExperimentConfig(**vars(args))
    cfg.log_self()
    return cfg
