from playwright.sync_api import expect

from test_UI_aliakseichaban_pw.pages.base_page import BasePage
from test_UI_aliakseichaban_pw.pages.locators import create_new_customer_locators as loc
from test_UI_aliakseichaban_pw.pages.locators import my_account_locators
from faker import Faker


class CreateCustomerAccount(BasePage):
    fake = Faker()
    f_name = fake.first_name()
    l_name = fake.last_name()
    address = fake.email()
    pwd = fake.password(8, True, True, True, True)
    confirm_pwd = pwd
    page_url = "/customer/account/create/"

    def fill_new_customer_account_form(self, f_name=f_name, l_name=l_name, address=address, pwd=pwd, confirm_pwd=pwd):
        self.enter_text(loc.f_name_field_loc, f_name)
        self.enter_text(loc.l_name_field_loc, l_name)
        self.enter_text(loc.address_field_loc, address)
        self.enter_text(loc.pwd_field_loc, pwd)
        self.enter_text(loc.pwd_confirmation_field_loc, confirm_pwd)

    def confirm_input(self):
        self.click(loc.create_btn_loc)

    def check_mandatory_fields_error_text(self, text):
        f_name_field = self.find_element(loc.f_name_field_error_loc)
        l_name_field = self.find_element(loc.l_name_field_error_loc)
        address_field = self.find_element(loc.address_field_error_loc)
        pwd_field = self.find_element(loc.pwd_field_error_loc)
        pwd_confirmation_field = self.find_element(loc.pwd_confirmation_field_error_loc)

        customer_fields_list = [f_name_field, l_name_field, address_field, pwd_field, pwd_confirmation_field]

        for field in customer_fields_list:
            expect(field).to_have_text(text), "There is no error for at least one field"

    def check_redirection_to_my_account_page(self):
        self.wait_for_element_is_present(my_account_locators.new_account_success_text_loc)

    def check_confirmation_pwd_error_text(self, text):
        error_loc = self.find_element(loc.pwd_confirmation_field_error_loc)
        expect(error_loc).to_have_text(text)
