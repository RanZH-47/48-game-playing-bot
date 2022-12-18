import time
from web_driver.web_driver import WebDriver
from web_driver.utils import Utils
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cookie:
    def __init__(self, url: str) -> None:
        self.url = url

    def select_language(self, web_driver, langauge_code: str):
        wait = WebDriverWait(web_driver, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "#loading")))
        
        langauge_option = web_driver.find_element(
            by=By.CSS_SELECTOR, value= "#langSelect-" + langauge_code
        )
        langauge_option.click()
        # handle loading screen

        wait = WebDriverWait(web_driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "cookieAnchor")))
    
    def get_cost(self, web_driver) -> float:
        cookie_amount = web_driver.find_element(by=By.CSS_SELECTOR, value="#cookies").text
        return Utils.extract_number(cookie_amount)

    def click_cookie(self, langauge_code: str):
        web_driver = WebDriver("Chrome").get_driver()
        # open a channel to url
        web_driver.get(self.url)
        # handle loading screen
        self.select_language(web_driver, langauge_code)
        timeout = time.time() + 5
        t_end = time.time() + 60 * 5
        time.sleep(2)
        cookie = web_driver.find_element(by=By.CSS_SELECTOR, value="#bigCookie")
        while True:
            cookie.click()
            if time.time() > timeout:
                try:
                    store_options = web_driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product'] .enabled")
                    store_options[-1].click()
                    timeout = time.time() + 1

                except IndexError:
                    cookie.click()
            if time.time() > t_end:
                break
        return web_driver        
