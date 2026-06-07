from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
driver.maximize_window()
blue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]")
blue_button.click()

sleep(5)
