from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()

# Открыть страницу
driver.get("https://the-internet.herokuapp.com/login")

sleep(2)

# Поиск поля Username
username = driver.find_element(By.ID, "username")

# Ввести "tomsmith" в поле username
you_name = "tomsmith"
username.send_keys(you_name)
sleep(2)

# Поиск поля Password
password = driver.find_element(By.ID, "password")

# Ввести "SuperSecretPassword!" в поле password
you_password = "SuperSecretPassword!"
password.send_keys(you_password)
sleep(2)

# Поиск кнопки Login
button_login = driver.find_element(By.CSS_SELECTOR, "i")
button_login.click()

# Проверка авторизации
success_message = driver.find_element(By.ID, "flash")
if "You logged into a secure area!" in success_message.text:
    print("Успешная авторизация!")
else:
    print("Ошибка авторизации.")
