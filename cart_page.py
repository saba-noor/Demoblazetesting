from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()

time.sleep(3)

driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()

time.sleep(2)
driver.find_element(By.LINK_TEXT, "Add to cart").click()

time.sleep(2)
try:
 alert = driver.switch_to.alert
 print("Alert", alert.text)
 alert.accept()
except:
 print("No alert.")

 driver.get("https://www.demoblaze.com/cart.html")

time.sleep(3)
items = driver.find_elements(By.CLASS_NAME, "success")
print("Cart Items: ")
for item in items:
    print("-", item.text)

time.sleep(3)
driver.quit()