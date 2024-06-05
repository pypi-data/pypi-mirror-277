#!/bin/python3
import argparse

try:
    # Attempt relative imports (if run as a package module)
    from .data import load_and_preprocess_data
    from .model_func import train_model
    from .utils import read_config, setup_logger

except ImportError:
    # Fallback to absolute imports (if run as a standalone script)
    from model_func import train_model
    from utils import read_config, setup_logger

    from data import load_and_preprocess_data

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(
        description="Train a U-net model from images and masks."
    )
    parser.add_argument("model_name", help="name of the model.")
    parser.add_argument(
        "-c",
        "--classes",
        default=["root"],
        help="Classes to use to train the model the model. For single class(recomended): ['class'], for multiclass(not advised):['class1', 'class2']",
    )
    parser.add_argument(
        "-d",
        "--patch_dir",
        default="./data_patched/",
        help="Path to data root directory, should end with '/'. Default: './data_patched/'",
        type=str,
    )

    parser.add_argument(
        "-s",
        "--seed",
        default=42,
        help="Seed for reading data and model training",
        type=int,
    )
    parser.add_argument(
        "-b",
        "--batch_size",
        default=16,
        help="What batch size to use. Default: 16",
        type=int,
    )

    parser.add_argument(
        "-e", "--epochs", default=20, help="Number of epochs. Default: 20", type=int
    )
    # Disabled
    parser.add_argument(
        "-r",
        "--roots",
        default=5,
        help="DISABLED!!! Number of expected plants inside petri dish. Default: 5",
    )

    args = parser.parse_args()
    model_name = args.model_name
    config = read_config(model_name)

    (
        train_generator,
        test_generator,
        steps_per_epoch,
        validation_steps,
    ) = load_and_preprocess_data(
        classes=args.classes,
        model_name=model_name,
        patch_size=config["input_shape"][0],
        patch_dir=args.patch_dir,
        seed=args.seed,
        batch_size=args.batch_size,
    )

    logger.info(f"Training model\n{steps_per_epoch = }\n{validation_steps = }")
    logger.info(config["input_shape"])

    train_model(
        model_name=model_name,
        train_generator=train_generator,
        test_generator=test_generator,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
        epochs=args.epochs,
    )


if __name__ == "__main__":
    main()
