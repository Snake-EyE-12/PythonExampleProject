from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://mcstacker.net/?cmd=give")

    # wait for the select to exist
    page.wait_for_selector("#GiveItem0")

    options = page.query_selector_all("#GiveItem0 option")

    items = [
        {
            "text": opt.inner_text().strip(),
            "value": opt.get_attribute("value")
        }
        for opt in options
    ]

    browser.close()

print(items)
