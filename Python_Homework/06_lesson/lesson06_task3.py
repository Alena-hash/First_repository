from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "spinner"))
    )

third_image = driver.find_elements(By.CSS_SELECTOR, "#image-container img")[2]

src_attribute = third_image.get_attribute("src")
print(src_attribute)

driver.quit()
