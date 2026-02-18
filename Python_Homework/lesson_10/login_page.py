import allure
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ввести логин: {username}")
    def enter_username(self, username):
        """Вводит имя пользователя."""
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        """"Вводит пароль пользователя"""
        self.driver.find_element(By.ID, "password").send_keys(password)

    @allure.step("Нажать кнопку Login")
    def click_login(self):
        """Нажимает кнопку входа."""
        self.driver.find_element(By.ID, "login-button").click()
