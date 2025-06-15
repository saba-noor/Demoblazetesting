from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()

time.sleep(3)
assert "STORE" in driver.title
print("Title Verified")
categories = driver.find_elements(By.CLASS_NAME, "list-group-item")
for cat in categories:
 print("Category:", cat.text)

time.sleep(3)
driver.quit()