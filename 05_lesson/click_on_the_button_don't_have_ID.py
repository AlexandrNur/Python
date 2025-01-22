from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Кликнуть на синюю кнопку
# Так как у кнопки динамический ID, то будем искать её по тексту
blue_button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
blue_button.click()
sleep(5)

# Вывести сообщение об успешном нажатии
print("Синяя кнопка была успешно нажата.")
