from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

# 1. Fill input boxes
driver.find_element(By.ID, "name").send_keys("Sudipa")
driver.find_element(By.ID, "email").send_keys("sudipa@gmail.com")
driver.find_element(By.ID, "phone").send_keys("9876543210")
driver.find_element(By.ID, "textarea").send_keys("Kolkata")

# 2. Select radio button
driver.find_element(By.ID, "female").click()

# 3. Select checkboxes
driver.find_element(By.ID, "sunday").click()
driver.find_element(By.ID, "monday").click()
driver.find_element(By.ID, "tuesday").click()

# 4. Scroll down
driver.execute_script("window.scrollBy(0,500)")

# 5. Date Picker 1
driver.find_element(By.ID, "datepicker").send_keys("08/31/2026")

# 6. Date Picker 2
driver.find_element(By.ID, "txtDate").send_keys("31/08/2026")

# 7. Scroll further down
driver.execute_script("window.scrollBy(0,500)")

# 8. Date Picker 3 - Start Date
driver.find_element(By.ID, "start-date").send_keys("08/31/2026")

# 9. Date Picker 3 - End Date
driver.find_element(By.ID, "end-date").send_keys("09/05/2026")

# 10. Click Submit
driver.find_element(By.XPATH, "//button[text()='Submit']").click()

time.sleep(3)

driver.quit()