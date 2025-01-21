from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome(options=options)

    return chrome_driver


def test_check_product_in_basket(driver):
    added_product_name = "Sony vaio i7"

    driver.get('https://www.demoblaze.com/index.html')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='tbodyid']/div/div/a")))
    list_of_products = driver.find_elements(By.XPATH, "//div[@id='tbodyid']/descendant::a[@class='hrefch']")
    url = list_of_products[-1].get_attribute("href")

    driver.execute_script(f'window.open("{url}", "_blank");')

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Add to cart')]")))
    add_to_cart_btn = driver.find_element(By.XPATH, "//a[contains(text(), 'Add to cart')]")
    add_to_cart_btn.click()

    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    driver.close()
    driver.switch_to.window(tabs[0])

    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='cartur']")))
    cart_btn = driver.find_element(By.XPATH, "//a[@id='cartur']")
    cart_btn.click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//tbody[@id='tbodyid']/tr[1]/td[2]")))
    product_in_cart = driver.find_element(By.XPATH, "//tbody[@id='tbodyid']/tr[1]/td[2]")

    assert added_product_name == product_in_cart.text, "The wrong product is added to the cart"


def test_product_to_compare(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='qc-cmp2-summary-buttons']/button[2]")))
    disagree_btn = driver.find_element(By.XPATH, "//div[@class='qc-cmp2-summary-buttons']/button[2]")
    disagree_btn.click()

    first_product = driver.find_element(By.XPATH, "//ol[contains(@class, 'products')]/li[1]")
    add_to_compare_btn = driver.find_element(
        By.XPATH, "//ol[contains(@class, 'products')]/li[1]/descendant::a[@title='Add to Compare']"
    )

    ActionChains(driver).move_to_element(first_product).click(add_to_compare_btn).perform()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//ol[contains(@class, 'products')]/li[1]")))
    first_product = driver.find_element(
        By.XPATH, "//ol[contains(@class, 'products')]/li[1]/descendant::a[@class='product-item-link']"
    )
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//ol[@id='compare-items']/descendant::a[text()='Push It Messenger Bag']"))
    )
    product_in_compare_section = driver.find_element(
        By.XPATH, "//ol[@id='compare-items']/descendant::a[text()='Push It Messenger Bag']"
    )

    assert first_product.text == product_in_compare_section.text, "Wrong product is added"
