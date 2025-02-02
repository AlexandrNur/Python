from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def test_saucedemo_checkout():
    # Инициализация веб-драйвера для Google Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # Открываем сайт магазина
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # Добавление товаров в корзину
        add_to_cart_buttons = [
            'add-to-cart-sauce-labs-backpack',
            'add-to-cart-sauce-labs-bolt-t-shirt',
            'add-to-cart-sauce-labs-onesie'
        ]

        for button_id in add_to_cart_buttons:
            driver.find_element(By.ID, button_id).click()

        # Переход в корзину
        cart_button = driver.find_element(By.ID, "shopping_cart_container")
        cart_button.click()

        # Нажатие Checkout
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Заполнение формы своими данными
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Иванов")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        # Получение итоговой суммы
        total_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text

        # Проверка итоговой суммы
        assert total_text == "Total: $58.29", f"Unexpected total amount: {total_text}"

    finally:
        # Закрываем браузер
        driver.quit()


# Для запуска тестирования через pytest
if __name__ == "__main__":
    pytest.main()
