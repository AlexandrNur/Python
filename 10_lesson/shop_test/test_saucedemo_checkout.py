import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import allure


@pytest.fixture
def driver():
    driver_instance = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver_instance
    driver_instance.quit()


@allure.title("Test SauceDemo процесс оформления заказа")
@allure.description("Тестирование всего процесса оформления заказа на сайте SauceDemo.")
@allure.feature("Кассовые тесты")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_checkout(driver):
    with allure.step("Войти в приложение"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart([
            'add-to-cart-sauce-labs-backpack',
            'add-to-cart-sauce-labs-bolt-t-shirt',
            'add-to-cart-sauce-labs-onesie'
        ])
        inventory_page.go_to_cart()

    with allure.step("Перейти к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.checkout()

    with allure.step("Заполните информацию о клиенте и продолжите"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_in_customer_info("Иван", "Иванов", "123456")

    with allure.step("Подтвердить общую сумму"):
        total_text = checkout_page.get_total()
        assert total_text == "Total: $58.29", f"Unexpected total amount: {total_text}"
