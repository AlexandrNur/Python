from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


# Открыть страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликнуть на кнопку "Add Element"
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()
    sleep(0.5)  # Небольшая задержка для надежности

# Собрать со страницы список кнопок "Delete"
delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

# Вывести на экран размер списка
print(f"Количество кнопок 'Delete': {len(delete_buttons)}")
