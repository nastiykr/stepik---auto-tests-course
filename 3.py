from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")

input1 = browser.find_element_by_name('firstname')
input1.send_keys("Ivan")

input2 = browser.find_element_by_name('lastname')
input2.send_keys("I")

input3 = browser.find_element_by_name('e-mail')
input3.send_keys("Isdsdds@hnfjkdsm")


elements = browser.find_elements_by_css_selector('.first_block > input[type="text"]')
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_css_selector("button.btn")
button.click()
# не забывайте добавлять пустую строку в конце каждого файла в Python
