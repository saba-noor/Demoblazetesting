from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.LINK_TEXT, "Contact").click()

time.sleep(2)
driver.find_element(By.ID, "recipient-email").send_keys("sneha@example.com")
driver.find_element(By.ID, "recipient-name").send_keys("Sneha Saxena")
driver.find_element(By.ID, "message-text").send_keys("Hello, this is a test message.")
driver.find_element(By.XPATH, "//button[text()='Send message']").click()

time.sleep(2)
try:
 alert = driver.switch_to.alert
 print("Alert", alert.text)
 alert.accept()
except:
 print("No alert appeared.")
driver.quit()