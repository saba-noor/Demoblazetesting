from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()

time.sleep(3)

driver.find_element(By.XPATH, "//a[text()='Laptops']").click()

time.sleep(2)
driver.find_element(By.LINK_TEXT, "Sony vaio i5").click()

time.sleep(3)
product_name = driver.find_element(By.TAG_NAME, "h2").text
description = driver.find_element(By.ID, "more-information").text
print("Product Name:", product_name)
print("Description:", description)

time.sleep(3)
driver.quit()