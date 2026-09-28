from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()

driver.maximize_window()

driver.get("https://text-compare.com/")

time.sleep(3)

# Locate left and right text boxes
left_text = driver.find_element(By.CSS_SELECTOR, "textarea:nth-of-type(1)")
right_text = driver.find_element(By.CSS_SELECTOR, "textarea:nth-of-type(2)")

act = ActionChains(driver)

# Task 1 - Type Welcome to Selenium on the left
act.click(left_text)

act.send_keys("Welcome to Selenium")

# Select all text from left side
act.key_down(Keys.CONTROL)

act.send_keys("a")

act.key_up(Keys.CONTROL)

# Copy the text
act.key_down(Keys.CONTROL)

act.send_keys("c")

act.key_up(Keys.CONTROL)

# Task 2 - Paste the copied text into the right side
act.click(right_text)

act.key_down(Keys.CONTROL)

act.send_keys("v")

act.key_up(Keys.CONTROL)

act.perform()

time.sleep(2)

# Task 3 - Scroll to the bottom of the webpage
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);"
)

time.sleep(2)

# Click About
about = driver.find_element(By.XPATH, "//a[text()='About']")
about.click()

time.sleep(3)

driver.quit()