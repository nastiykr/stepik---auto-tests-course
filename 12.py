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



current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)
