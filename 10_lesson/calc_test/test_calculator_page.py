import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage
import allure


@pytest.fixture
def driver():
    driver_instance = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver_instance
    driver_instance.quit()


@allure.title("Тестирование функциональности калькулятора")
@allure.description("Тестирование основных операций калькулятора с задержкой.")
@allure.feature("Тесты Калькулятора")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver):
    with allure.step("Откройте страницу калькулятора"):
        page = CalculatorPage(driver)
        page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    with allure.step("Установить задержку срабатывания"):
        page.set_delay("45")

    with allure.step("Выполнить расчет"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Получить и проверить результат"):
        result = page.get_result("15")
        assert result == "15", f"Expected result to be 15, but got {result}"
