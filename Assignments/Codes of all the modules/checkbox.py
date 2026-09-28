from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

# Find all checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# Click all checkboxes
for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()

time.sleep(2)

driver.quit()