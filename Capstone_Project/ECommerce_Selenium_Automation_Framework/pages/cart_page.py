from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_LINK_IN_HEADER = (By.CSS_SELECTOR, "#header-cart a")
    CART_DROPDOWN_ITEMS = (By.CSS_SELECTOR, "#header-cart ul.dropdown-menu li")
    CART_TABLE_ROWS = (By.CSS_SELECTOR, "#content table tbody tr")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "#content p")
    SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert.alert-success")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url

    def get_add_to_cart_confirmation(self):
        """
        Return the text of the success alert that OpenCart shows right
        after 'Add to Cart' is clicked (e.g. "Success: You have added ...").
        Returns an empty string if no alert appears in time.
        """
        if self.is_element_present(self.SUCCESS_ALERT, timeout=10):
            return self.get_text(self.SUCCESS_ALERT)
        return ""

    def open_cart_page(self):
        """Navigate directly to the full shopping cart page."""
        self.open(self.base_url.rstrip("/") + "/index.php?route=checkout/cart")

    def get_cart_item_count(self):
        """Return the number of product rows shown in the cart table."""
        rows = self.driver.find_elements(*self.CART_TABLE_ROWS)
        return len(rows)

    def get_cart_row_texts(self):
        """Return the visible text of every row in the cart table."""
        rows = self.driver.find_elements(*self.CART_TABLE_ROWS)
        return [row.text for row in rows]
