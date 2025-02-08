import re
from playwright.sync_api import expect

from test_UI_aliakseichaban_pw.pages.base_page import BasePage
from test_UI_aliakseichaban_pw.pages.locators import sale_locators as loc


class SalePage(BasePage):
    page_url = "/sale.html"

    def check_categories_presence(self, list_of_categories):
        categories = self.find_elements(loc.available_categories_loc)
        for category in categories:
            assert category.text_content() in list_of_categories, "Some of the categories is wrong or isn't present"

    def check_sale_is_selected(self):
        element = self.find_element(loc.sale_in_navigation_section_loc)
        expect(element).to_have_class(re.compile(r".*\bactive\b.*"))


    def check_sale_page_title(self, sale_page_name):
        self.wait_for_text_in_element(loc.sale_title_loc, sale_page_name), "The wrong page title"


    def open_privacy_policy(self):
        self.click(loc.privacy_btn_loc)

    def check_policy_parameters_off(self):
        self.wait_for_element_is_present(loc.first_policy_loc)
        first = self.find_element(loc.first_policy_loc)
        second = self.find_element(loc.second_policy_loc)
        third = self.find_element(loc.third_policy_loc)
        list_of_policies = [first, second, third]

        for policy in list_of_policies:
            expect(policy).to_have_text("OFF"), "Policy status is wrong"
