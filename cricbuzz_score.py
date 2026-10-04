from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        channel="msedge",
        headless=False
    )

    page = browser.new_page()
    page.goto("https://www.cricbuzz.com")

    print(page.title())

    page.screenshot(path="score.png")
    browser.close()