import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from data_types_page import DataTypesPage
import allure


@pytest.fixture
def driver():
    driver_instance = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver_instance
    driver_instance.quit()


@allure.title("Тестовые типы данных Форма отправки")
@allure.description("Тестирует отправку форм типов данных и проверки полей.")
@allure.feature("Тесты по подаче форм")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission(driver):
    with allure.step("Страница формы открытых типов данных"):
        page = DataTypesPage(driver)
        page.open("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    with allure.step("Заполните и отправьте форму"):
        page.fill_form()
        page.submit_form()

    with allure.step("Проверьте цвета полей формы"):
        zip_code_color = page.get_border_color("zip-code")
        assert zip_code_color == "rgb(245, 194, 199)", f"Expected red border for zip code, got {zip_code_color}"

        expected_green_color = "rgb(186, 219, 204)"

        for field in page.fields:
            if field == "zip-code":
                continue
            field_color = page.get_border_color(field)
            assert field_color == expected_green_color, f"Expected green border for {field}, got {field_color}"
