from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        """
        :param driver: Веб-драйвер для взаимодействия с браузером.
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self) -> None:
        """
        Метод открытия страницы входа.
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Метод входа в приложение.
        :param username: str, Имя пользователя.
        :param password: str, Пароль пользователя.
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
