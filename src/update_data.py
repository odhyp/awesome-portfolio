import json
import re


def read_markdown_table(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

        # Filter out lines that are part of the table and remove any alignment row
        table_lines = [line.strip() for line in lines if "|" in line]
        table_lines = [
            line for line in table_lines if not re.match(r"\|?\s*-+\s*\|", line)
        ]

        if len(table_lines) < 2:
            raise ValueError("Markdown file does not contain a valid table!")

        # Extract headers
        headers = [col.strip() for col in table_lines[0].split("|") if col.strip()]

        # Extract rows
        data = []
        for line in table_lines[1:]:
            values = [col.strip() for col in line.split("|") if col.strip()]
            if len(values) == len(headers):
                data.append(dict(zip(headers, values)))

        return data


def save_to_json(data: dict, output_file: str):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# FIXME: Don't run it here, move it to main.py instead.
def main():
    markdown_file = "README.md"
    output_json = "data/portfolio.json"

    try:
        table_data = read_markdown_table(markdown_file)
        save_to_json(table_data, output_json)
        print(f"Table data saved to {output_json}")

    except Exception as e:
        print(f"Error: {e}")
