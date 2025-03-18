from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        """
        :param driver: Веб-драйвер для взаимодействия с браузером.
        """
        self.driver = driver
        self.cart_button = (By.ID, "shopping_cart_container")

    def add_to_cart(self, product_ids: list) -> None:
        """
        Метод добавления продуктов в корзину.
        :param product_ids: list, Список идентификаторов продуктов для добавления в корзину.
        """
        for product_id in product_ids:
            self.driver.find_element(By.ID, product_id).click()

    def go_to_cart(self) -> None:
        """
        Метод перехода на страницу корзины.
        """
        self.driver.find_element(*self.cart_button).click()
