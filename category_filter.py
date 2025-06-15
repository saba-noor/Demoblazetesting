from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

categories = ["cat", "itemc"]  # "cat" is the ID of the categories div, "itemc" is the class of each category link

category_names = ["Phones", "Laptops", "Monitors"]
for category_name in category_names:
 # Find category element by link text
 category_element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, category_name)))
 category_element.click()
# Wait for products to load under selected category

time.sleep(3)  # simple wait to allow page refresh
print(f"Category: {category_name}")
# List visible product names after category filter
products = driver.find_elements(By.CSS_SELECTOR, ".card-title")
for product in products:
 print(f"- {product.text}")
driver.quit()
