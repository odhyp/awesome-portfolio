from playwright.sync_api import sync_playwright


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


# FIXME: Don't run it here, move it to main.py instead.
def main():
    url = "https://odhyp.com"
    output_path = "screenshot.png"

    take_screenshot(url, output_path)
