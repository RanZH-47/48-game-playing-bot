import constants
from web_driver.web_driver import WebDriver
from web_driver.utils import Utils
from selenium.webdriver.common.by import By


class Amazon:
    def __init__(self, url: str) -> None:
        self.url = url

    def get_unit_price(self) -> float:
        web_driver = WebDriver("Chrome").get_driver()
        # open a channel to url
        web_driver.get(self.url)
        price_text = web_driver.find_element(by=By.ID, value=constants.PRICE_ID).text
        price = Utils.extract_number(price_text)
        web_driver.close()
        return price
