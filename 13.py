from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element_by_css_selector("button.btn")
button1.click()

alert = browser.switch_to.alert
alert.accept()

x = browser.find_element_by_id("input_value").text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

input = browser.find_element_by_id('answer')
input.send_keys(y) 

button2 = browser.find_element_by_css_selector("button.btn")
button2.click()
