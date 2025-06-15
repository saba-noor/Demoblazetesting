from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# --- Click Sign up ---
wait.until(EC.element_to_be_clickable((By.ID, "signin2"))).click()
wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))

username = "BCAstudent123"
password = "bca@123"
driver.find_element(By.ID, "sign-username").send_keys(username)

driver.find_element(By.ID, "sign-password").send_keys(password)
driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
# --- Accept Alert ---
try:

 WebDriverWait(driver, 5).until(EC.alert_is_present())

 alert = driver.switch_to.alert

 print("Signup Alert:", alert.text)

 alert.accept()

except:

 print("No alert appeared.")

time.sleep(3)