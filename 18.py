from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest


class TestAbs(unittest.TestCase):
	def test_abs1(self):
	
		link = 'http://suninjuly.github.io/registration1.html'
		browser = webdriver.Chrome()
		browser.get(link)
		
		# Ваш код, который заполняет обязательные поля
		input1 = browser.find_element_by_css_selector('.first_block .first')
		input1.send_keys("Ivan")
		input2 = browser.find_element_by_css_selector('.first_block .second')
		input2.send_keys("Petrov")
		input3 = browser.find_element_by_css_selector('.first_block .third')
		input3.send_keys("Smolensk")
		
        	# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		
		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)
		
		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual(browser.find_element_by_tag_name("h1").text, "Поздравляем! Вы успешно зарегистировались!", 'Error Registration 1')

	def test_abs2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)
		
		# Ваш код, который заполняет обязательные поля
		input1 = browser.find_element_by_css_selector('.first_block .first')
		input1.send_keys("Ivan")
		input2 = browser.find_element_by_css_selector('.first_block .second')
		input2.send_keys("Petrov")
		input3 = browser.find_element_by_css_selector('.first_block .third')
		input3.send_keys("Smolensk")
		
        	# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		
		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)
		
		self.assertEqual(browser.find_element_by_tag_name("h1").text, "Поздравляем! Вы успешно зарегистировались!", 'Error Registration 1')
        
if __name__ == "__main__":
	unittest.main()



