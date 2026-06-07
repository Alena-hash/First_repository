from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")
input_field = driver.find_element(By.TAG_NAME, "input")
sleep(3)

input_field.send_keys("Sky")
sleep(3)

input_field.clear()
sleep(3)

input_field.send_keys("Pro")
sleep(3)

driver.quit()
