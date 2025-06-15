from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 40)  # Increased from 20 to 40 seconds

wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys("BCAstudent123")
driver.find_element(By.ID, "loginpassword").send_keys("bca@123")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()

time.sleep(5)  # Increased pause for login completion
# Select first product on homepage
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='tbodyid']/div[1]/div/a"))).click()

time.sleep(3)  # Buffer before adding to cart
# Click 'Add to cart'
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))).click()
# Accept alert confirming add to cart
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
print("Alert:", alert.text)
alert.accept()

time.sleep(4)  # Extra wait for cart update
driver.find_element(By.ID, "cartur").click()  # Go to cart page

time.sleep(5)  # Give time for cart page to load
# Click Place Order button
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))).click()
# Fill order form details
wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Saba")
driver.find_element(By.ID, "country").send_keys("India")
driver.find_element(By.ID, "city").send_keys("Delhi")
driver.find_element(By.ID, "card").send_keys("1234 5678 9012 3456")
driver.find_element(By.ID, "month").send_keys("12")
driver.find_element(By.ID, "year").send_keys("2025")
# Click Purchase
driver.find_element(By.XPATH, "//button[text()='Purchase']").click()
# Confirm order success message
success = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "sweet-alert")))
print("Order Confirmation:", success.text)

time.sleep(5)
# Close confirmation popup
driver.find_element(By.XPATH, "//button[text()='OK']").click()

time.sleep(2)
driver.quit()