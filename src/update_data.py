import re

from src.utils import save_to_json, ensure_folder_exists


def read_markdown_table(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    table_lines = [line.strip() for line in lines if "|" in line]

    # Remove any alignment row (e.g., | --- | --- |)
    table_lines = [line for line in table_lines if not re.match(r"\|?\s*-+\s*\|", line)]

    if len(table_lines) < 2:
        raise ValueError("Markdown file does not contain a valid table!")

    data = []
    for line in table_lines[1:]:
        values = [col.strip() for col in line.split("|") if col.strip()]
        if values:
            modified_entry = {
                "author": values[0] if values else "",
                "liveName": (
                    re.search(r"\[(.*?)\]", values[1]).group(1)
                    if len(values) > 1
                    else ""
                ),
                "liveUrl": (
                    re.search(r"\((.*?)\)", values[1]).group(1)
                    if len(values) > 1
                    else ""
                ),
                "sourceName": (
                    re.search(r"\[(.*?)\]", values[2]).group(1)
                    if len(values) > 2
                    else ""
                ),
                "sourceUrl": (
                    re.search(r"\((.*?)\)", values[2]).group(1)
                    if len(values) > 2
                    else ""
                ),
                "techStack": (
                    [s.strip() for s in values[3].split(",")]
                    if len(values) > 3
                    else "[]"
                ),
            }
            data.append(modified_entry)

    return data


def main():
    output_dir = "data"
    markdown_file = "README.md"
    output_json = f"{output_dir}/portfolio.json"

    try:
        ensure_folder_exists(output_dir)
        table_data = read_markdown_table(markdown_file)
        save_to_json(table_data, output_json)
        print(f"Table data saved to {output_json}")

    except Exception as e:
        print(f"Error: {e}")
