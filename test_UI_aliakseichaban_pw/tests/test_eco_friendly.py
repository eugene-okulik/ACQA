def test_sort_by_price_desc_direction(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.decline_privacy_policy()
    eco_friendly_page.sort_clothes_by("price")
    eco_friendly_page.set_descending_direction()
    eco_friendly_page.check_sorting_by_price_desc()

def test_add_to_cart_confirmation_message(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.decline_privacy_policy()
    eco_friendly_page.select_xs_size_first_color_for_last_clothe_on_page_and_add_to_cart()
    eco_friendly_page.check_clothe_added_message()


def test_remove_all_from_cart(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.decline_privacy_policy()
    eco_friendly_page.select_xs_size_first_color_for_last_clothe_on_page_and_add_to_cart()
    eco_friendly_page.open_not_empty_cart()
    eco_friendly_page.remove_the_first_clothe_from_cart()
    eco_friendly_page.check_cart_is_empty()
    eco_friendly_page.check_counter_is_not_visible()
