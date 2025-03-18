from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        """
        :param driver: Веб-драйвер для взаимодействия с браузером.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def checkout(self) -> None:
        """
        Способ перехода к оформлению заказа со страницы корзины.
        """
        self.driver.find_element(*self.checkout_button).click()
