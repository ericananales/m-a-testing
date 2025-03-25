from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Provide the full path to ChromeDriver (Modify if needed)
chrome_driver_path = "C:\\Users\\Acer\\Documents\\chromedriver.exe"

# Initialize WebDriver using Service()
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

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
