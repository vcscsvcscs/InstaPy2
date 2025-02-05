""" Module that handles the like features """
# import built-in & third-party modules

# import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# import InstaPy2 modules
from .util import update_activity

LIKE_TAG_CLASS = "coreSpriteHeartOpen"


def get_like_on_feed(browser, amount):
    """
    browser - the selenium browser element
    amount - total amount of likes to perform

    --------------------------------------
    The function takes in the total amount of likes to perform
    and then sends buttons to be liked, if it has run out of like
    buttons it will perform a scroll
    """
    assert 1 <= amount

    likes_performed = 0
    while likes_performed != amount:
        try:
            like_buttons = browser.find_elements(By.CLASS_NAME, LIKE_TAG_CLASS)
        except NoSuchElementException:
            print("Unable to find the like buttons, aborting")
            break
        else:
            for button in like_buttons:
                likes_performed += 1
                if amount < likes_performed:
                    print("Performed the required number of likes")
                    break
                yield button

            print("--> Total Likes uptil now ->", likes_performed)

            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            update_activity(browser, state=None)
