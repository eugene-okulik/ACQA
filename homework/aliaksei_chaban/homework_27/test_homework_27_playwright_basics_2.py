from playwright.sync_api import Page, expect, BrowserContext


# Задание 1
def test_confirm_modal(page: Page):
    page.on("dialog", lambda alert: alert.accept())
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.wait_for_selector("//a[text()='Click']")
    page.locator("//a[text()='Click']").click()
    text = page.locator("//p[@id='result-text']")
    expect(text).to_have_text("Ok")


# Задание 2
def test_switch_tabs(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    new_page_link = page.get_by_role("link", name="Click")
    with context.expect_page() as new_page_event:
        new_page_link.click()
    new_page = new_page_event.value
    expected_text = new_page.locator("//p[@id='result-text']")
    expect(expected_text).to_have_text("I am a new page in a new tab")
    expect(new_page_link).to_be_enabled()


# Задание 3
def test_color_change(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    button = page.locator("//button[@id='colorChange']")
    expect(button).to_have_class("mt-4 text-danger btn btn-primary")
    button.click()
