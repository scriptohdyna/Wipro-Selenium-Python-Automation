from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browsername = "chrome"

# create actions for chrome or firefox browsers
if browsername.lower() == "chrome":
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

elif browsername.lower() == "firefox":
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )

else:
    raise Exception(
        "Invalid browser name. Please choose 'chrome' or 'firefox'."
    )

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

# clicking on the selected radio button (Button number 2)
driver.find_element(By.XPATH, "//input[@value='radio2']").click()

time.sleep(2)

driver.quit()