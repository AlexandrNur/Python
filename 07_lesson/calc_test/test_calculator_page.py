import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver_instance = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver_instance
    driver_instance.quit()


def test_calculator(driver):
    page = CalculatorPage(driver)
    page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    page.set_delay("45")
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.get_result("15")
    assert result == "15", f"Expected result to be 15, but got {result}"
