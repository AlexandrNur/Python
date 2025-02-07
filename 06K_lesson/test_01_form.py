from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def test_form_submission():
    # Инициализация веб-драйвера для Google Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # Открываем указанную страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Объект, хранящий данные для заполнения формы
        field_data = {
            'first-name': 'Иван',
            'last-name': 'Петров',
            'address': 'Ленина, 55-3',
            'e-mail': 'test@skypro.com',
            'phone': '+7985899998787',
            'zip-code': '',  # Оставляем пустым
            'city': 'Москва',
            'country': 'Россия',
            'job-position': 'QA',
            'company': 'SkyPro'
        }

        # Заполнение формы данными из словаря field_data
        for name, value in field_data.items():
            field = driver.find_element(By.NAME, name)  # Находим элемент по имени
            field.clear()  # Очищаем поле от предзаполненных данных
            field.send_keys(value)  # Вводим значение

        # Нажимаем кнопку Submit
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()

        # Проверяем, что поле Zip code подсвечено красным
        zip_code_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'zip-code'))
        )
        red_border_color = zip_code_field.value_of_css_property("border-color")
        assert red_border_color == "rgb(245, 194, 199)", (
            f"Expected red border color, but got {red_border_color}")

        # Проверяем, что все остальные поля подсвечены зеленым
        expected_green_color = "rgb(186, 219, 204)"
        for name in field_data:
            if name == "zip-code":
                continue
            field = driver.find_element(By.ID, name)
            green_border_color = field.value_of_css_property("border-color")
            assert green_border_color == expected_green_color, (
                f"Expected green border color for field {name}, but got {green_border_color}")

    finally:
        # Закрываем браузер
        driver.quit()


# Для запуска тестирования через pytest
if __name__ == "__main__":
    pytest.main()
