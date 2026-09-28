# ECommerce Selenium Automation Framework

A beginner-friendly Selenium + Python test automation framework developed for the **Wipro Capstone Assignment: Selenium Python Framework Development using Unittest, PyTest, and the Page Object Model (POM)**.

**Site under test:** https://tutorialsninja.com/demo/
**Browser:** Google Chrome
**Automation tools:** Selenium WebDriver, PyTest, Unittest

## 1. Project Structure

```text
ECommerce_Selenium_Automation_Framework/
│
├── config/
│   └── config.ini
│
├── data/
│   └── test_data.csv
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── search_page.py
│   └── cart_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_registration.py
│   ├── test_login.py
│   ├── test_search.py
│   ├── test_cart.py
│   └── test_smoke_unittest.py
│
├── utils/
│   ├── config_reader.py
│   ├── csv_reader.py
│   └── screenshot.py
│
├── reports/
├── screenshots/
│
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## 2. Framework Overview

The framework uses the **Page Object Model (POM)** to separate page-specific locators and interactions from test cases. Shared browser actions and helper methods are maintained in `pages/base_page.py`, while assertions are placed in the test files.

PyTest fixtures in `tests/conftest.py` manage the browser setup and teardown for PyTest tests. The framework also includes a separate Unittest smoke test that manages its own browser session.

## 3. Prerequisites

* Python 3.14
* Google Chrome installed
* A project virtual environment (`venv`)
* Selenium, PyTest, and pytest-html installed in the virtual environment

Selenium Manager can automatically manage the ChromeDriver download in supported environments. If it cannot download the driver, manual ChromeDriver setup may be required.

## 4. Set Up the Environment

Open PowerShell or Command Prompt in the project root directory.

Activate the virtual environment:

```powershell
venv\Scripts\activate
```

Check that the required packages are installed:

```powershell
pip show selenium pytest pytest-html
```

If any required packages are missing, install them using:

```powershell
pip install -r requirements.txt
```

## 5. Running the Tests

Run the complete PyTest suite from the project root:

```powershell
python -m pytest -v
```

Run a specific test file:

```powershell
python -m pytest tests/test_login.py -v
```

Run a single test:

```powershell
python -m pytest tests/test_search.py::test_search_for_product_shows_results -v
```

Run the standalone Unittest smoke test:

```powershell
python -m unittest tests.test_smoke_unittest -v
```

PyTest can also discover and run the Unittest smoke test as part of the full suite.

## 6. HTML Reports and Screenshots

To generate a self-contained HTML report, run:

```powershell
python -m pytest -v --html=reports/report.html --self-contained-html
```

The generated report is saved in the `reports/` directory.

Screenshots are saved in the `screenshots/` directory. The PyTest fixture hook captures screenshots automatically when a PyTest test fails. The utility `utils/screenshot.py` also provides screenshot functionality for tests that call it directly.

## 7. Configuration and Test Data

### Configuration

The `config/config.ini` file stores the base URL, browser settings, and placeholder login credentials.

You can update the base URL or browser settings in this file when needed. The invalid login credentials are sample values used for testing login rejection. Do not store real passwords in the project’s tracked configuration files.

### CSV Test Data

The `data/test_data.csv` file contains sample placeholder data for tests, such as registration details and search keywords. The `utils/csv_reader.py` utility reads the CSV file and returns its rows as dictionaries for use in tests.

The registration happy-path test generates a unique placeholder email for each run to reduce conflicts with previously created demo accounts.


