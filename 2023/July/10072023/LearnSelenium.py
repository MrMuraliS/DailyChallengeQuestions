from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Safari()
driver.maximize_window()
driver.get("https://demostore.x-cart.com/")
currency = driver.find_element(By.XPATH, '//*[@id="header-bar"]/div[2]/a')
currency.click()
dropdown_element = driver.find_element(By.XPATH, '//*[@id="currency_code_1"]')
dropdown = Select(dropdown_element)
text = dropdown.first_selected_option.get_attribute("text")
print(text)
assert text == "US Dollar"
time.sleep(3)
