from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Locate the product table
table = wait.until(
    EC.presence_of_element_located((By.ID, "productTable"))
)

# Scroll to table
driver.execute_script(
    "arguments[0].scrollIntoView();", table
)

time.sleep(2)

# IDs to select
target_ids = ["1", "3", "5"]

# Find rows
rows = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//table[@id='productTable']/tbody/tr")
    )
)

for row in rows:
    row_id = row.find_element(By.XPATH, "./td[1]").text.strip()

    if row_id in target_ids:
        checkbox = row.find_element(
            By.XPATH, "./td[4]//input[@type='checkbox']"
        )

        if not checkbox.is_selected():
            checkbox.click()

        print("Selected ID:", row_id)

time.sleep(3)

driver.quit()