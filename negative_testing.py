from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
# --- Negative Login ---
wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))

driver.find_element(By.ID, "loginusername").send_keys("wronguser")
driver.find_element(By.ID, "loginpassword").send_keys("wrongpass")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
# Handle login alert
try:
 WebDriverWait(driver, 5).until(EC.alert_is_present())
 alert = driver.switch_to.alert
 print("Login Alert (Invalid creds):", alert.text)
 alert.accept()
except:
 print("No alert on invalid login.")
 # Manually close login modal (press X button)
try:
 close_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logInModal"]//button[@class="close"]')))
 close_button.click()
except:
 print("Login modal close button not found or not clickable.")

time.sleep(1)  # let it close
# --- Negative Signup ---
wait.until(EC.element_to_be_clickable((By.ID, "signin2"))).click()
wait.until(EC.visibility_of_element_located((By.ID, "sign-username")))
driver.find_element(By.ID, "sign-username").send_keys("BCAstudent123")
driver.find_element(By.ID, "sign-password").send_keys("somepass")
driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
# Handle signup alert
try:
 WebDriverWait(driver, 5).until(EC.alert_is_present())
 alert = driver.switch_to.alert
 print("Signup Alert (Existing user):", alert.text)
 alert.accept()
except:
 print("No alert on signup.")
 driver.quit()
