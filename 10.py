from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id('num1')
x = x_element.text

y_element = browser.find_element_by_id('num2')
y = y_element.text

def calc(x,y):
  return str(int(x) + int(y))

z = calc(x,y)

browser.find_element_by_tag_name("select").click()

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(z)

button = browser.find_element_by_css_selector("button.btn")
button.click()