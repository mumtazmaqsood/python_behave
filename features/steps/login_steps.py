from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Lunch chrome browser1')
def lunch_browser1(context):
    path = "C:\\python310\\libs\\chromedriver.exe"
    context.driver = webdriver.Chrome(path)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

@when('Open homepage1')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@when('Enter username "{user}" & password "{pwd}"')
def enter_credentials(context, user, pwd):
    context.driver.find_element(By.NAME, "username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)

@when('Click on login button')
def click_login(context):
    context.driver.find_element(By.XPATH, "//button[text()=' Login ']").click()


@then('user successfully login to the Dashboard page')
def chk_dashboard(context):
    try:
        tag_name = context.driver.find_element(By.TAG_NAME, "h6").text
        assert tag_name == "PIM"
        # assert True, "Test Passed"
    except:
        context.driver.close()
        assert False, "Test Failed"
    # if tag_name == "PIM":
    #     context.driver.close()
    #     assert True, "Test Passed"

