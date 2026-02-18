import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ввести имя: {first_name}")
    def enter_first_name(self, first_name):
        """Вводит имя покупателя."""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)

    @allure.step("Ввести фамилию: {last_name}")
    def enter_last_name(self, last_name):
        """Вводит фамилию покупателя."""
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)

    @allure.step("Ввести почтовый индекс: {postal_code}")
    def enter_postal_code(self, postal_code):
        """Вводит почтовый индекс."""
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    @allure.step("Нажать кнопку Finish")
    def click_finish(self):
        """Завершает оформление заказа."""
        self.driver.find_element(By.CSS_SELECTOR, ".cart_button").click()

    @allure.step("Получить итоговую сумму")
    def get_total(self):
        """Возвращает текст с итоговой суммой заказа."""
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")
            )
        )
        return total_element.text
