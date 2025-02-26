from datetime import datetime
from pathlib import Path

from src.utils import read_json


def create_markdown(portfolio_data: dict):
    title = portfolio_data["author"]
    author = portfolio_data["author"]
    live_name = portfolio_data["liveName"]
    live_url = portfolio_data["liveUrl"]
    source_name = portfolio_data["sourceName"]
    source_url = portfolio_data["sourceUrl"]
    tags = portfolio_data["techStack"]

    front_matter = f"""+++
title = "{title}"
author = "{author}"
liveName = "{live_name}"
liveUrl = "{live_url}"
sourceName = "{source_name}"
sourceUrl = "{source_url}"
tags = {tags}
+++
"""

    file_name = title.lower().replace(" ", "-")
    file_path = Path(f"site/content/{file_name}.md")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(front_matter)


def main():
    portfolio_list = read_json("data/portfolio.json")

    for item in portfolio_list:
        create_markdown(item)


if __name__ == "__main__":
    main()
