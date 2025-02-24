from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.buttons = {
            "7": (By.XPATH, '//span[text()="7"]'),
            "+": (By.XPATH, '//span[text()="+"]'),
            "8": (By.XPATH, '//span[text()="8"]'),
            "=": (By.XPATH, '//span[text()="="]')
        }
        self.result_screen = (By.CSS_SELECTOR, '.screen')

    def open(self, url):
        self.driver.get(url)

    def set_delay(self, delay):
        input_element = self.driver.find_element(*self.delay_input)
        input_element.clear()
        input_element.send_keys(delay)

    def click_button(self, button):
        self.driver.find_element(*self.buttons[button]).click()

    def get_result(self, expected_result, timeout=60):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.result_screen, expected_result))
        return self.driver.find_element(*self.result_screen).text
