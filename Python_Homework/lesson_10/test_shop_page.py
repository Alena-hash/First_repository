import allure
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage

@allure.epic("Sauce Demo")
@allure.feature("Покупка товаров")
@allure.title("Сквозной сценарий покупки")
@allure.description("Авторизация, добавление 3-х товаров в корзину и проверка финальной суммы")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop_purchase():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    main_page = MainPage(driver)
    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item in items:
        main_page.add_item_to_cart(item)
    main_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_first_name("Алена")
    checkout_page.enter_last_name("Тарасова")
    checkout_page.enter_postal_code("123456")
    checkout_page.click_finish()

    with allure.step("Проверить итоговую сумму заказа"):
        total_text = checkout_page.get_total()
    assert "$58.29" in total_text, (
       f"Итоговая сумма не равна $58.29,"
       f"а равна {total_text}"
    )

    driver.quit()
