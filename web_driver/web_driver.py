from pathlib import Path
from typing import Union

from selenium import webdriver
from selenium.webdriver.common.service import Service

import constants


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
