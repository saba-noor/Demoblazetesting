from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 30)  # Increased wait time to 30 seconds

try:
 # Scroll to bottom of page to ensure footer is visible
 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

 time.sleep(8)  # Increased sleep to 5 seconds for safety
# Wait for the footer element (by tag name or class if needed)

 footer = wait.until(EC.presence_of_element_located((By.TAG_NAME, "footer")))
# Optional: Validate some footer text or attribute to be extra sure
 footer_text = footer.text

 print("Footer found with text preview:", footer_text[:60])  # Show first 60 chars

except Exception as e:
 print("Error: Footer not found.")
 print(f"Details: {e}")

finally:
 driver.quit()
