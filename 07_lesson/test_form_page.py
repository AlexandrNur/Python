import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_form_submission(driver):
    page = FormPage(driver)
    page.open("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

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

    page.fill_form(field_data)
    page.submit_form()

    assert page.get_field_border_color('zip-code') == "rgb(245, 194, 199)", "Expected red border color."

    expected_green_color = "rgb(186, 219, 204)"
    for name in field_data:
        if name == 'zip-code':
            continue
        assert page.get_field_border_color(name) == expected_green_color, f"Expected green border color for field {name}."