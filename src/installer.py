import subprocess
import sys


def install_packages(packages: list, install_playwright: bool = False):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", *packages])

        if install_playwright:
            subprocess.check_call(
                [sys.executable, "-m", "playwright", "install", "chromium"]
            )

    except subprocess.CalledProcessError as e:
        print(f"Failed to install packages: {e}")
        sys.exit(1)
