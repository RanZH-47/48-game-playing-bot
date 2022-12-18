# on amazon page,
# test case 1: find price
# test case 2: find css yellow
# test case 3: find a href link
import pytest

import constants
from web_driver.amazon import Amazon


def test_get_price(target_price):
    scraped_price = Amazon(constants.PS4_URL).get_unit_price()
    assert scraped_price == target_price
