from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument("--force-device-scale-factor=0.7")
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome(options=options)
    # chrome_driver.implicitly_wait(5)

    return chrome_driver


# ----------------------------- 1st task ----------------------------
def test_input_result(driver):
    input_data = "Hello"
    driver.get("https://www.qa-practice.com/elements/input/simple")

    text_string = driver.find_element(By.XPATH, "//input[@id='id_text_string']")
    text_string.send_keys(input_data)
    text_string.submit()
    text_result = driver.find_element(By.XPATH, "//p[@id='result-text']")
    assert text_result.text == input_data

    print(text_result.text)


# ----------------------------- 2nd task ----------------------------

def test_form_result(driver):
    my_f_name = 'Aliaksei'
    my_s_name = 'Chaban'
    my_email_address = 'test@gtest.com'
    my_phone_number = '1234567890'
    my_subject = 'English'
    my_address = "Szczecin, Poland, Zlotowska 99/9, 55-555"
    my_month = "June"
    my_year = "1995"
    my_day = "023"

    driver.get("https://demoqa.com/automation-practice-form")

    first_name = driver.find_element(By.XPATH, "//input[@id='firstName']")
    first_name.send_keys(my_f_name)

    second_name = driver.find_element(By.XPATH, "//input[@id='lastName']")
    second_name.send_keys(my_s_name)

    email = driver.find_element(By.XPATH, "//input[@id='userEmail']")
    email.send_keys(my_email_address)

    gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    gender.click()

    mobile = driver.find_element(By.XPATH, "//input[@id='userNumber']")
    mobile.send_keys(my_phone_number)

    date_of_birth_field = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
    date_of_birth_field.click()
    date_month = driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']")
    select_month = Select(date_month)
    select_month.select_by_visible_text(my_month)
    date_year = driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']")
    select_year = Select(date_year)
    select_year.select_by_visible_text(my_year)
    date_day = driver.find_element(By.XPATH, f"//div[contains(@class,'react-datepicker__day--{my_day}')]")
    date_day.click()

    subject = driver.find_element(By.XPATH, "//div[@id='subjectsContainer']/descendant::input")
    subject.send_keys(my_subject)
    wait = WebDriverWait(driver, 5)
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='react-select-2-option-0']"))
    )
    subject_dropdown = driver.find_element(By.XPATH, "//div[@id='react-select-2-option-0']")
    subject_dropdown.click()

    hobbies = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
    hobbies.click()

    current_address = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
    current_address.send_keys(my_address)

    state = driver.find_element(By.XPATH, "//div[@id='state']")
    state.click()
    state_option = driver.find_element(By.XPATH, "//div[@id='react-select-3-option-1']")
    state_option.click()

    city = driver.find_element(By.XPATH, "//div[@id='city']")
    city.click()
    state_option = driver.find_element(By.XPATH, "//div[@id='react-select-4-option-0']")
    state_option.click()

    submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
    submit_button.click()

    table_values = driver.find_element(By.XPATH, "//div[@class='modal-content']")
    print(table_values.text)


# ----------------------------- 3rd task ----------------------------

def test_language_choice(driver):
    language = "Python"

    driver.get('https://www.qa-practice.com/elements/select/single_select')

    language_field = driver.find_element(By.XPATH, "//select[@id='id_choose_language']")
    lang_dropdown = Select(language_field)
    lang_dropdown.select_by_visible_text(language)

    submit_btn = driver.find_element(By.XPATH, "//input[@id='submit-id-submit']")
    submit_btn.click()

    my_choice = driver.find_element(By.XPATH, "//p[@id='result-text']")
    assert my_choice.text == language, "The wrong language is selected"


def test_hello_world_presence(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    wait = WebDriverWait(driver, 10)

    start_btn = driver.find_element(By.XPATH, "//button")
    start_btn.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']")))
    hello_text = driver.find_element(By.XPATH, "//div[@id='finish']/h4")

    assert hello_text.text == "Hello World!", "There is a wrong message"
