from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_id("input_value").text


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


y = calc(x)


input3 = browser.find_element_by_id('answer')
input3.send_keys(y) 

option1 = browser.find_element_by_id('robotCheckbox')
option1.click()

option2 = browser.find_element_by_css_selector("[for='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
