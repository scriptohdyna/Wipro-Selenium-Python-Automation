"""
screenshot.py

Small utility for saving a screenshot to the screenshots/ folder. The
folder path is resolved relative to the project root (see
utils/config_reader.py) so it never hard-codes a Windows username or
absolute path.
"""

import os
from datetime import datetime

from utils.config_reader import PROJECT_ROOT


def take_screenshot(driver, name="screenshot"):
    screenshots_dir = os.path.join(PROJECT_ROOT, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = "".join(c if c.isalnum() or c in ("-", "_") else "_" for c in name)
    file_name = f"{safe_name}_{timestamp}.png"
    file_path = os.path.join(screenshots_dir, file_name)

    driver.save_screenshot(file_path)
    return file_path
