from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()

time.sleep(3)
# Click on the Phones tab
phones_tab = driver.find_element(By.XPATH, "//a[text()='Phones']")
phones_tab.click()

time.sleep(3)
# Scroll down to load all products
last_height = driver.execute_script("return document.body.scrollHeight")


while True:
    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for Loading

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # Exit if no more content is loaded
    last_height = new_height

# Now capture all product names
products = driver.find_elements(By.CLASS_NAME, "card-title")
print("Available Products:")
for product in products:
 print("-", product.text)

time.sleep(2)
driver.quit()
