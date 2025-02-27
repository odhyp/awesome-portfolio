import argparse
import importlib

from src.installer import install_packages


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--update-data", action="store_true", help="Run the update_data function"
    )
    parser.add_argument(
        "--update-ss", action="store_true", help="Run the update_ss function"
    )
    parser.add_argument(
        "--update-site", action="store_true", help="Run the update_site function"
    )

    args = parser.parse_args()

    if args.update_data:
        update_data = importlib.import_module("src.update_data")
        update_data.main()

    if args.update_ss:
        requirements = ["playwright"]
        install_packages(requirements, install_playwright=True)

        update_ss = importlib.import_module("src.update_ss")
        update_ss.main()

    if args.update_site:
        update_site = importlib.import_module("src.update_site")
        update_site.main()


if __name__ == "__main__":
    main()
