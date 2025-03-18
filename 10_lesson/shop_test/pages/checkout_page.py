from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        """
        :param driver: Веб-драйвер для взаимодействия с браузером.
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_in_customer_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Метод заполнения формы информации о клиенте.
        :param first_name: str, Имя клиента.
        :param last_name: str, Фамилия клиента.
        :param postal_code: str, Почтовый индекс клиента.
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self) -> str:
        """
        Метод получения общей стоимости из сводки оформления заказа.
        :return: str, Общая стоимость, отображаемая в сводке.
        """
        return self.driver.find_element(*self.total_label).text
