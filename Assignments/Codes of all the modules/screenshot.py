from selenium import webdriver
import os
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(2)

folder = r"C:\Users\SUDIPA DEB\OneDrive\Pictures\Screenshots"

os.makedirs(folder, exist_ok=True)

file_path = os.path.join(folder, "homepage.png")

result = driver.save_screenshot(file_path)

print("Screenshot saved:", result)
print("Location:", file_path)
print("File exists:", os.path.exists(file_path))

time.sleep(2)

driver.quit()