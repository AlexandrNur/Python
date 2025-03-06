from selenium.webdriver.common.by import By


class DataTypesPage:
    def __init__(self, driver):
        self.driver = driver
        self.fields = {
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
        self.submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')

    def open(self, url):
        self.driver.get(url)

    def fill_form(self):
        for name, value in self.fields.items():
            field = self.driver.find_element(By.NAME, name)
            field.clear()
            field.send_keys(value)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()

    def get_border_color(self, field_name):
        field = self.driver.find_element(By.ID, field_name)
        return field.value_of_css_property("border-color")
