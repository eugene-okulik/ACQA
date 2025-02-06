from playwright.sync_api import Page, expect, Route
import json


def test_changed_title(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = "яблокофон 16 про"
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route("**/step0_iphone/digitalmat**", handle_route)
    page.goto("https://www.apple.com/shop/buy-iphone")
    page.hover("//h3[contains(text(), 'Pro')]")
    page.click("//button[@data-trigger-id='digitalmat-1']")
    title = page.locator("//h2[@data-autom='DigitalMat-overlay-header-0-0']")
    expect(title).to_be_visible()
    expect(title).to_have_text("яблокофон 16 про")
