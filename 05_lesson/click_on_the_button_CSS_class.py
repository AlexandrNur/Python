from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


# Открыть страницу
driver.get("http://uitestingplayground.com/classattr")

# Кликнуть на синюю кнопку.
# Используем класс 'btn-primary' для поиска
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
blue_button.click()
sleep(5)

# Вывести сообщение об успешном нажатии
print("Синяя кнопка была успешно нажата.")
