def test_create_new_customer_valid(create_new_customer_page):
    create_new_customer_page.open_page()
    create_new_customer_page.decline_privacy_policy()
    create_new_customer_page.fill_new_customer_account_form()
    create_new_customer_page.confirm_input()
    create_new_customer_page.check_redirection_to_my_account_page()


def test_required_fields_errors_check(create_new_customer_page):
    create_new_customer_page.open_page()
    create_new_customer_page.decline_privacy_policy()
    create_new_customer_page.confirm_input()
    create_new_customer_page.check_mandatory_fields_error_text("This is a required field.")


def test_confirmation_pwd_missmatch(create_new_customer_page):
    create_new_customer_page.open_page()
    create_new_customer_page.decline_privacy_policy()
    create_new_customer_page.fill_new_customer_account_form(confirm_pwd="wrong")
    create_new_customer_page.confirm_input()
    create_new_customer_page.check_confirmation_pwd_error_text("Please enter the same value again.")
