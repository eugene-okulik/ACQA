import pytest
from test_UI_aliakseichaban_pw.pages.create_new_customer import CreateCustomerAccount
from test_UI_aliakseichaban_pw.pages.eco_friendly import EcoFriendlyClothes
from test_UI_aliakseichaban_pw.pages.sale import SalePage


@pytest.fixture()
def create_new_customer_page(page):
    return CreateCustomerAccount(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendlyClothes(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)
