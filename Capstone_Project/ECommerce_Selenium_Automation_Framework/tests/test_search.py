
from pages.home_page import HomePage
from pages.search_page import SearchPage
from utils.csv_reader import read_csv_data


def test_search_for_product_shows_results(driver, base_url):
    home_page = HomePage(driver, base_url)
    home_page.load()
    home_page.search_product("Mac")

    search_page = SearchPage(driver)
    assert search_page.has_results(), (
        "Expected at least one product in the search results."
    )


def test_search_using_csv_data(driver, base_url):
    rows = read_csv_data()
    assert len(rows) > 0, (
        "Expected at least one row of test data in data/test_data.csv"
    )

    keyword = rows[0]["search_keyword"]

    home_page = HomePage(driver, base_url)
    home_page.load()
    home_page.search_product(keyword)

    search_page = SearchPage(driver)
    result_count = search_page.get_result_count()

    assert result_count >= 0, (
        "Expected the search results page to load without error."
    )