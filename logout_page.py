from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Setup
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
# Login first (Assuming user exists)
wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys("BCAstudent123")
driver.find_element(By.ID, "loginpassword").send_keys("bca@123")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
# Wait for login to complete (Check if 'Welcome username' appears)
welcome_text = wait.until(EC.visibility_of_element_located((By.ID, "nameofuser"))).text
print("Login successful:", welcome_text)

time.sleep(2)  # Let page stabilize
# Click Logout
wait.until(EC.element_to_be_clickable((By.ID, "logout2"))).click()
# Verify logout success: Login button visible again
login_button_visible = wait.until(EC.visibility_of_element_located((By.ID, "login2")))
print("Logout successful, login button displayed:", login_button_visible.is_displayed())

time.sleep(2)  # Just for observation
# Close browser
driver.quit()