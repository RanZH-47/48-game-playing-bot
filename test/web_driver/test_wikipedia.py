# on wikpedia page,
# test case 1: find how many articles are in English in total
import constants
from web_driver.wikipedia import Wikipedia


def test_get_article_number(target_number):
    scraped_number = Wikipedia(constants.WIKI_URL).get_article_number()
    # target number in 2022/12/13
    assert scraped_number >= target_number


def test_search_wikipedia():
    search_result = Wikipedia(constants.WIKI_URL).search_wikipedia("Michael")
    assert constants.NO_SEARCH_RESULT_INFO not in search_result
