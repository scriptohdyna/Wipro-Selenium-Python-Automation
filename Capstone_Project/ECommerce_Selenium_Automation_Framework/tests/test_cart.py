from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.cart_page import CartPage


def test_add_product_to_cart(driver, base_url):
    home_page = HomePage(driver, base_url)
    home_page.load()
    home_page.search_product("Mac")

    search_page = SearchPage(driver)
    assert search_page.has_results(), "Need at least one search result to add to the cart."

    search_page.add_first_result_to_cart()

    cart_page = CartPage(driver, base_url)
    confirmation = cart_page.get_add_to_cart_confirmation()
    assert confirmation != "", "Expected a confirmation message after adding a product to the cart."
    assert "success" in confirmation.lower() or "added" in confirmation.lower(), (
        f"Expected an 'added to cart' style confirmation, got: '{confirmation}'"
    )

    cart_page.open_cart_page()
    item_count = cart_page.get_cart_item_count()
    assert item_count >= 1, "Expected at least one item in the cart after adding a product."
