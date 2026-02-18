import allure
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажать на кнопку Checkout")
    def click_checkout(self) -> None:
        """НажимаеЕ на кнопку оформления заказа."""
        self.driver.find_element(By.ID, "checkout").click()
