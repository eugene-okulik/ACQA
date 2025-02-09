def test_available_categories(sale_page):
    sale_page.open_page()
    sale_page.decline_privacy_policy()
    sale_page.check_categories_presence(["Women's Deals", "Mens's Deals", "Gear Deals"])


def test_sale_is_selected_in_navigation_section(sale_page):
    sale_page.open_page()
    sale_page.decline_privacy_policy()
    sale_page.check_sale_is_selected()


def test_sale_page_title(sale_page):
    sale_page.open_page()
    sale_page.decline_privacy_policy()
    sale_page.check_sale_page_title("Sale")


def test_policy_is_off_in_modal_window(sale_page):
    sale_page.open_page()
    sale_page.decline_privacy_policy()
    sale_page.open_privacy_policy()
    sale_page.check_policy_parameters_off()
