import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from calculator_page import CalculatorPage

@allure.epic("Тесты интерфейса")
@allure.feature("Калькулятор")
@allure.title("Проверка суммы чисел")
@allure.description("Сложение 7 и 8 с ожиданием результата")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator():
    driver = webdriver.Chrome()
    page = CalculatorPage(driver)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html")

    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    with allure.step("Ожидание появления результата 15"):
        wait = WebDriverWait(driver, 45)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"),
            "15"
        )
            )

    with allure.step("Сравнение полученного результата с эталоном"):
        result = page.get_result()

    assert result == "15"

    driver.quit()
