from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    RESULT_PRODUCTS = (By.CSS_SELECTOR, "div.product-thumb")
    NO_RESULTS_TEXT = (By.CSS_SELECTOR, "#content p")
    FIRST_PRODUCT_LINK = (By.CSS_SELECTOR, "div.product-thumb h4 a")
    FIRST_PRODUCT_ADD_TO_CART = (By.CSS_SELECTOR, "div.product-thumb button[onclick*='cart.add']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_result_count(self):
        """Return how many product tiles are shown on the results page."""
        products = self.driver.find_elements(*self.RESULT_PRODUCTS)
        return len(products)

    def has_results(self):
        """Return True if at least one product tile is present."""
        return self.get_result_count() > 0

    def open_first_result(self):
        """Click into the first product returned by the search."""
        self.click(self.FIRST_PRODUCT_LINK)

    def add_first_result_to_cart(self):
        """Click the 'Add to Cart' button on the first product tile."""
        self.click(self.FIRST_PRODUCT_ADD_TO_CART)
