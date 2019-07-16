from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element_by_css_selector("button.trollface")
button1.click()

window_name = browser.window_handles[1]
browser.switch_to.window(window_name)

x = browser.find_element_by_css_selector("label span.nowrap:nth-child(2)").text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

input = browser.find_element_by_id("answer")
input.send_keys(y) 

button2 = browser.find_element_by_css_selector("button.btn")
button2.click()
