from playwright.sync_api import expect

from test_UI_aliakseichaban_pw.pages.base_page import BasePage
from test_UI_aliakseichaban_pw.pages.locators import eco_friendly_locators as loc


class EcoFriendlyClothes(BasePage):
    page_url = "/collections/eco-friendly.html"
    expected_message = "You have no items in your shopping cart."

    def sort_clothes_by(self, option_value):
        self.select_from_dropdown_by_value(loc.sort_by_dropdown_loc, option_value)
        element = self.find_element("//option[@value='price']")
        expect(element.first).to_have_attribute("selected", "selected")

    def set_descending_direction(self):
        locator = self.find_element(loc.desc_sorting_btn_loc)
        locator.first.click()

    def select_xs_size_first_color_for_last_clothe_on_page_and_add_to_cart(self):
        self.on_hover(loc.last_clothe_on_page_loc)
        self.click(loc.last_clothe_xs_size_loc)
        self.click(loc.last_clothe_first_color_loc)
        self.click(loc.add_to_cart_btn_loc)

    def check_sorting_by_price_desc(self):
        prices = self.find_elements(loc.clothes_price_loc)
        prices_list = []
        for price in prices:
            price_to_float = float(price.text_content().replace("$", ""))
            prices_list.append(price_to_float)
        sorted_prices_list = sorted(prices_list, reverse=True)
        assert prices_list == sorted_prices_list, "Prices sorted incorrectly"

    def check_clothe_added_message(self):
        clothe_name = self.get_text(loc.last_clothe_name_loc)
        self.wait_for_element_is_present(loc.add_success_message_loc)

        success_msg = self.find_element(loc.add_success_message_loc)
        expect(success_msg).to_have_text(
            f"You added {clothe_name} to your shopping cart."), "The wrong message text is displayed"

    def open_not_empty_cart(self):
        self.wait_for_class_to_disappear(loc.cart_counter_parent_loc, "empty")
        self.wait_for_text_in_element(loc.cart_counter_child_loc, "1")
        self.click(loc.my_cart_loc)

    def remove_the_first_clothe_from_cart(self):
        self.wait_for_element_to_be_clickable(loc.remove_btn_loc)
        self.click(loc.remove_btn_loc)
        self.wait_for_element_to_be_clickable(loc.confirm_modal_loc)
        self.click(loc.confirm_modal_loc)

    def check_cart_is_empty(self):
        self.wait_for_element_is_present(loc.empty_cart_block_loc)
        self.wait_for_element_is_present(loc.empty_cart_text_loc)
        element = self.find_element(loc.empty_cart_text_loc)
        expect(element).to_have_text(self.expected_message)

    def check_counter_is_not_visible(self):
        element = self.find_element(loc.cart_counter_parent_loc)
        expect(element).not_to_be_visible()
