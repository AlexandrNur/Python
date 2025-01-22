from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()

# Открыть страницу
driver.get("https://the-internet.herokuapp.com/entry_ad")

sleep(3)

# Кликнуть на кнопку 'Close' в модальном окне
close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer > p")
close_button.click()

# Вывести сообщение об успешном закрытии модального окна
print("Модальное окно было закрыто.")
