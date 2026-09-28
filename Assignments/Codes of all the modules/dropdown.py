from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

# Select Option1 from dropdown
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown.select_by_visible_text("Option1")

time.sleep(2)

driver.quit()