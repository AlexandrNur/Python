from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()

# Открыть страницу
driver.get("https://the-internet.herokuapp.com/inputs")

sleep(2)

# Поиск поля ввода
input_filed = driver.find_element(By.CSS_SELECTOR, "input")

# Кликнуть на поле ввода
input_filed.click()

# Ввести "1000" в поле ввода
input_1 = "1000"
input_filed.send_keys(input_1)
sleep(2)

# Очистить поле ввода
input_filed.clear()
sleep(2)

# Ввести "999" в поле ввода
input_2 = "999"
input_filed.send_keys(input_2)

# Вывести сообщение об успешном вводе
print("Текст успешно введен")
