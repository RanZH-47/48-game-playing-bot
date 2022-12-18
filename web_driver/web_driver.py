from selenium import webdriver


class WebDriver:
    def __init__(self, broswer: str) -> None:
        if broswer == "Chrome":
            self.driver = webdriver.Chrome()
        if broswer == "Firefox":
            self.driver = webdriver.Firefox()
        if broswer == "Safari":
            self.driver = webdriver.Safari()

    def get_driver(self):
        return self.driver
