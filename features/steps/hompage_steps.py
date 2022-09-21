from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('launch chrome browser')
def launch_browser(context):
    path = "C:\\python310\\libs\\chromedriver.exe"
    context.driver = webdriver.Chrome(path)
    context.driver.implicitly_wait(5)

@when('open homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then('verify that the logo present on the page')
def verify_logo(context):
    get_img = context.driver.find_element(By.TAG_NAME, "img").is_displayed()
    # get_img = context.driver.find_element(By.XPATH, "//button[text()=' Login ']").is_displayed()
    assert get_img is True

@then('close browser')
def close_browser(context):
    context.driver.close()
