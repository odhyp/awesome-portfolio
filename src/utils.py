import json

from pathlib import Path


def ensure_folder_exists(folder_name: str):
    folder = Path(folder_name)
    folder.mkdir(parents=True, exist_ok=True)


def read_json(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def save_to_json(data: dict, output_file: str):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
