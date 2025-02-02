from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def test_calculator():
    # Инициализируем веб-драйвер для Google Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # Открываем указанную страницу калькулятора
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Вводим значение 45 в поле задержки
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажимаем кнопку '7'
        button_7 = driver.find_element(By.XPATH, '//span[text()="7"]')
        button_7.click()

        # Нажимаем кнопку '+'
        button_plus = driver.find_element(By.XPATH, '//span[text()="+"]')
        button_plus.click()

        # Нажимаем кнопку '8'
        button_8 = driver.find_element(By.XPATH, '//span[text()="8"]')
        button_8.click()

        # Нажимаем кнопку '='
        button_equals = driver.find_element(By.XPATH, '//span[text()="="]')
        button_equals.click()

        # Ожидаем появления результата '15' в течение 50 секунд (можете также установить 45 или больше для надежности)
        result = WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), "15")
        )

        # Убедимся, что результат действительно '15'
        assert result, "Calculation result is not 15."

    finally:
        # Закрываем браузер
        driver.quit()


# Для запуска тестирования через pytest
if __name__ == "__main__":
    pytest.main()
