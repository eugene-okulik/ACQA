from playwright.sync_api import Page, Locator, expect

disagree_btn_loc = "//div[@class='qc-cmp2-summary-buttons']/button[2]"


class BasePage:
    base_url = "https://magento.softwaretestingboard.com"
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError("Page can not be opened for this page class")

    def decline_privacy_policy(self):
        self.page.wait_for_selector(disagree_btn_loc)
        dis_btn = self.find_element(disagree_btn_loc)
        dis_btn.click()
        expect(dis_btn).not_to_be_visible()

    def find_element(self, locator) -> Locator:
        return self.page.locator(locator)

    def find_elements(self, locator):
        return self.page.query_selector_all(locator)

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.find_element(locator).fill(text)

    def get_title(self):
        return self.page.title()

    def get_text(self, locator):
        return self.page.text_content(locator)

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def select_from_dropdown_by_value(self, dropdown_loc, option):
        self.page.select_option(dropdown_loc, option)

    def on_hover(self, on_hover_element_loc):
        element = self.find_element(on_hover_element_loc)
        element.hover()

    def wait_for_element_is_present(self, locator):
        element = self.find_element(locator)
        expect(element).to_be_visible()

    def wait_for_class_to_disappear(self, locator, class_to_disappear):
        element = self.find_element(locator)
        expect(element).not_to_have_class(class_to_disappear)

    def wait_for_text_in_element(self, locator, text):
        element = self.page.locator(locator)
        expect(element).to_have_text(text)

    def wait_for_element_to_be_clickable(self, locator):
        loc = self.page.locator(locator)
        expect(loc).to_be_enabled()
