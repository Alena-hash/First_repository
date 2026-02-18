import allure
from selenium.webdriver.common.by import By


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Установить задержку ожидания: {seconds} сек.")
    def set_delay(self, seconds):
        """
        Очищает поле задержки и вводит новое значение.
        :param seconds: количество секунд (целое число)"""
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay"
                                 ).send_keys(str(seconds))

    @allure.step("Нажать на кнопку: {text}")
    def click_button(self, text):
        """Находит кнопку калькулятора по тексту на ней и нажимает.
        :param text: текст на кнопке (например, '7', '+', '=')"""
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    @allure.step("Считать результат с экрана")
    def get_result(self):
        """Получает текущий текст, отображаемый на экране калькулятора.
        :return: строковое значение результата"""
        return self.driver.find_element(By.CLASS_NAME, "screen").text
