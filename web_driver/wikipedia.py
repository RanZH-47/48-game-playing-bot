import constants
from web_driver.web_driver import WebDriver
from web_driver.utils import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Wikipedia:
    def __init__(self, url: str) -> None:
        self.url = url

    def get_article_number(self) -> str:
        web_driver = WebDriver("Chrome").get_driver()
        # open a channel to url
        web_driver.get(self.url)
        article_number_text = web_driver.find_element(
            by=By.CSS_SELECTOR, value="#articlecount a:nth-child(1)"
        ).get_attribute("text")
        article_number = Utils.extract_number(article_number_text)
        web_driver.close()
        return article_number

    def search_wikipedia(self, keyword: str) -> str:
        web_driver = WebDriver("Chrome").get_driver()
        # open a channel to url
        web_driver.get(self.url)
        search_box = web_driver.find_element(
            by=By.CSS_SELECTOR, value="#simpleSearch input:nth-child(1)"
        )
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)
        search_page_source = web_driver.page_source
        web_driver.close()
        return search_page_source
