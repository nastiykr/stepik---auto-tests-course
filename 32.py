import pytest
from selenium import webdriver
import time
import math

answer = math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('intput', ["236895", "236896","236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, input):
    link = "https://stepik.org/lesson/{}/step/1/".format(input)
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")