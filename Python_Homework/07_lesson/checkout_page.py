from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def click_finish(self):
        self.driver.find_element(By.CSS_SELECTOR, ".cart_button").click()

    def get_total(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")
            )
        )
        return total_element.text
