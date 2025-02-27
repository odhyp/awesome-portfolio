from playwright.sync_api import sync_playwright

from src.utils import read_json, ensure_folder_exists


def take_screenshot(url: str, output_path: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto(url, timeout=60_000, wait_until="networkidle")
            page.screenshot(path=output_path, full_page=False)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()


def main(update_type: str = "latest"):
    output_dir = "site/static/ss"
    ensure_folder_exists(output_dir)

    portfolio_json = "data/portfolio.json"
    portfolio_data = read_json(portfolio_json)

    if update_type == "latest":
        latest_data = portfolio_data[-1]

        url = latest_data["liveUrl"]
        ss_name = latest_data["liveName"]
        output_path = f"{output_dir}/{ss_name}.png"

        try:
            take_screenshot(url, output_path)
            print(f"Update Screenshot: {url} saved as {output_path}")
        except Exception as e:
            print(f"Update Screenshot failed: {e}")

    if update_type == "all":
        for data in portfolio_data:
            url = data["liveUrl"]
            ss_name = data["liveName"]
            output_path = f"{output_dir}/{ss_name}.png"

            try:
                take_screenshot(url, output_path)
                print(f"Update Screenshot: {url} saved as {output_path}")
            except Exception as e:
                print(f"Update Screenshot failed: {e}")
