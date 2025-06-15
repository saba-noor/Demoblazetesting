from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# --- Setup ---
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# --- Click Login ---
wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
# --- Credentials ---
username = "BCAstudent123"
password = "bca@123"
driver.find_element(By.ID, "loginusername").send_keys(username)
driver.find_element(By.ID, "loginpassword").send_keys(password)
driver.find_element(By.XPATH, "//button[text()='Log in']").click()

# --- Confirm Login Success ---
try:
 welcome = wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
 print(" Login successful:", welcome.text)
except:  #  FIXED: Added colon
 print(" Login failed.")


time.sleep(5)
driver.quit()
