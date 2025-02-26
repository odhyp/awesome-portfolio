import argparse

from src.installer import install_packages
from src.utils import read_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--update-data", action="store_true", help="Run the update_data function"
    )

    args = parser.parse_args()

    if args.update_data:
        requirements = ["rich"]
        install_packages(requirements)
        print("Called function update data")


if __name__ == "__main__":
    main()
