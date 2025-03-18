from selenium.webdriver.common.by import By


class DataTypesPage:
    def __init__(self, driver):
        """
        :param driver: Веб-драйвер для взаимодействия с браузером.
        """
        self.driver = driver
        self.fields = {
            'first-name': 'Иван',
            'last-name': 'Петров',
            'address': 'Ленина, 55-3',
            'e-mail': 'test@skypro.com',
            'phone': '+79858999987',
            'zip-code': '',  # Оставляем пустым
            'city': 'Москва',
            'country': 'Россия',
            'job-position': 'QA',
            'company': 'SkyPro'
        }
        self.submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')

    def open(self, url: str) -> None:
        """
        Метод открытия страницы формы типов данных.
        :param url: str, URL-адрес открываемой страницы.
        """
        self.driver.get(url)

    def fill_form(self) -> None:
        """
        Метод заполнения формы предопределенными данными.
        """
        for name, value in self.fields.items():
            field = self.driver.find_element(By.NAME, name)
            field.clear()
            field.send_keys(value)

    def submit_form(self) -> None:
        """
        Способ отправки формы.
        """
        self.driver.find_element(*self.submit_button).click()

    def get_border_color(self, field_name: str) -> str:
        """
        Метод получения цвета границы поля формы.
        :param field_name: str, Имя поля.
        :return: str, Значение свойства цвета границы CSS.
        """
        field = self.driver.find_element(By.ID, field_name)
        return field.value_of_css_property("border-color")
