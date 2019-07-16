from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

message = WebDriverWait(browser, 18).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000"))

button = browser.find_element_by_id("book")
button.click()



x = browser.find_element_by_css_selector("label span.nowrap:nth-child(2)").text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

input = browser.find_element_by_id("answer")
input.send_keys(y) 

button2 = browser.find_element_by_id("solve")
button2.click()