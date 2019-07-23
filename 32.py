import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()




@pytest.mark.parametrize('input', ["895","896", "897", "898","899", "903", "904", "905"])
def test_guest_should_see_login_link(browser, input):
	link = "https://stepik.org/lesson/236{}/step/1/".format(input)
	browser.implicitly_wait(10)
	browser.get(link)
	input = browser.find_element_by_css_selector("textarea.textarea")
	
	answer = math.log(int(time.time()))
	input.send_keys(str(answer))
	
	button = browser.find_element_by_css_selector(".submit-submission")
	button.click()
	assert browser.find_element_by_css_selector(".smart-hints__hint").text == "Correct!"