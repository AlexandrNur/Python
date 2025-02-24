import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from data_types_page import DataTypesPage


@pytest.fixture
def driver():
    driver_instance = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver_instance
    driver_instance.quit()


def test_form_submission(driver):
    page = DataTypesPage(driver)
    page.open("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    page.fill_form()
    page.submit_form()

    # Проверка, что поле Zip code подсвечено красным
    zip_code_color = page.get_border_color("zip-code")
    assert zip_code_color == "rgb(245, 194, 199)", f"Expected red border for zip code, got {zip_code_color}"

    # Проверка, что остальные поля подсвечены зеленым
    expected_green_color = "rgb(186, 219, 204)"

    for field in page.fields:
        if field == "zip-code":
            continue
        field_color = page.get_border_color(field)
        assert field_color == expected_green_color, f"Expected green border for {field}, got {field_color}"
