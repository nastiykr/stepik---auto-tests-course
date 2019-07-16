from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import os 

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

option1 = browser.find_element_by_name('firstname')
option1.send_keys("Ivan")

option2 = browser.find_element_by_name('lastname')
option2.send_keys("Petrov")

option3 = browser.find_element_by_name('email')
option3.send_keys("Isdsdds@hnfjkdsm")
option3 = browser.find_element_by_name('file')


current_dir = os.path.abspath(os.path.dirname("C:\\"))
file_path = os.path.join(current_dir, 'file.txt') 
option3.send_keys(file_path)

option4 = browser.find_element_by_css_selector("button.btn")
option4.click()