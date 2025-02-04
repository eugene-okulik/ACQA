from playwright.sync_api import Page


# Задание 1
def test_first_task(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='Username').fill('Alex-Test')
    page.get_by_role('textbox', name='Password').fill('Second-Name')
    page.get_by_role('button', name='Login').click()


# Задание 2
def test_second_task(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Alex')
    page.get_by_placeholder('Last Name').fill('Test')
    page.get_by_placeholder('name@example.com').fill('test@test.qwe')
    page.get_by_text('Other').click()
    page.get_by_placeholder('Mobile Number').fill('1234567890')
    page.wait_for_selector("//input[@id='dateOfBirthInput']")
    page.locator("//input[@id='dateOfBirthInput']").click()
    page.select_option("//select[@class='react-datepicker__month-select']", value="5")
    page.select_option("//select[@class='react-datepicker__year-select']", value="1994")
    page.locator("//div[text()='23']").click()
    page.locator("//input[@id='subjectsInput']").fill("eng")
    page.locator("//div[@id='react-select-2-option-0']").click()
    page.locator("//label[text()='Music']").click()
    page.get_by_placeholder('Current Address').fill('Zlotowska 101/1')
    page.locator("//div[@id='state']").click()
    page.locator("//div[@id='react-select-3-option-1']").click()
    page.locator("//div[@id='city']").click()
    page.locator("//div[@id='react-select-4-option-2']").click()
    page.wait_for_selector("//button[text()='Submit']")
    page.get_by_role("button", name="Submit").click()
