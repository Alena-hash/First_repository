import allure
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Добавить товар в корзину: {item_name}")
    def add_item_to_cart(self, item_name):
        """Ищет товар по имени и нажимает кнопку добавления в корзину."""
        self.driver.find_element(
            By.XPATH,
            f"//div[text()='{item_name}']/"
            "ancestor::div[@class='inventory_item']//button"
        ).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """Нажимает на иконку корзины."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
