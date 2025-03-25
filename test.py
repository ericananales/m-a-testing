from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # If ChromeDriver is not in PATH, specify the full path: webdriver.Chrome(executable_path="C:\\Users\\Acer\\Documents\\chromedriver.exe")

# Open the web application
driver.get("http://127.0.0.1:5000/login")

# Locate username, password, and login button
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "//input[@type='submit']")

# Enter login credentials
username.send_keys("testuser")
password.send_keys("password123")
login_button.click()

# Wait for the page to load
time.sleep(2)

# Check if login was successful
if "Dashboard" in driver.page_source:
    print("✅ Login Test Passed")
else:
    print("❌ Login Test Failed")

# Close the browser
driver.quit()
