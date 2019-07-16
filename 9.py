from selenium import webdriver
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

robots_radio = browser.find_element_by_id("treasure")
x = robots_radio.get_attribute("valuex")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


y = calc(x)


input3 = browser.find_element_by_id('answer')
input3.send_keys(y) 

option1 = browser.find_element_by_id('robotCheckbox')
option1.click()

option2 = browser.find_element_by_id('robotsRule')
option2.click()


button = browser.find_element_by_css_selector("button.btn")
button.click()