from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR, "input#newButtonName.form-control")
input_field.clear()
input_field.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "button#updatingButton.btn.btn-primary")
button.click()

updated_button = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

final_button_text = driver.find_element(By.ID, "updatingButton").text
print(final_button_text)
driver.quit()
