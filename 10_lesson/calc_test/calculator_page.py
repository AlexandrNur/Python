from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        """
        :param driver: Веб-драйвер для взаимодействия с браузером.
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.buttons = {
            "7": (By.XPATH, '//span[text()="7"]'),
            "+": (By.XPATH, '//span[text()="+"]'),
            "8": (By.XPATH, '//span[text()="8"]'),
            "=": (By.XPATH, '//span[text()="="]')
        }
        self.result_screen = (By.CSS_SELECTOR, '.screen')

    def open(self, url: str) -> None:
        """

        Метод открытия страницы калькулятора.
        :param url: str, URL-адрес открываемой страницы.
        """
        self.driver.get(url)

    def set_delay(self, delay: str) -> None:
        """
        Метод установки задержки в операциях.
        :param delay: str, Время задержки, которое необходимо установить.
        """
        input_element = self.driver.find_element(*self.delay_input)
        input_element.clear()
        input_element.send_keys(delay)

    def click_button(self, button: str) -> None:
        """
        Метод нажатия кнопки калькулятора.
        :param button: str, Текст кнопки для нажатия.
        """
        self.driver.find_element(*self.buttons[button]).click()

    def get_result(self, expected_result: str, timeout: int = 60) -> str:
        """
        Метод получения результата с дисплея калькулятора.
        :param expected_result: str, Ожидаемый результат для отображения.
        :param timeout: int, Время ожидания результата.
        :return: str, Результат, отображаемый на калькуляторе.
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.result_screen, expected_result))
        return self.driver.find_element(*self.result_screen).text
