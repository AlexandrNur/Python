from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.ID, "shopping_cart_container")

    def add_to_cart(self, product_ids):
        for product_id in product_ids:
            self.driver.find_element(By.ID, product_id).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
