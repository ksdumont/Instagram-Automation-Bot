import time
import random
from util.comments import *
from selenium.webdriver.common.keys import Keys


def comment_on_photo(browser):
    sleepy_time = 5
    comment = 0

    try:
        text_box = browser.find_element_by_class_name("Ypffh")
        time.sleep(sleepy_time)
        text_box.click()
        text_box = browser.find_element_by_class_name("Ypffh")
        time.sleep(sleepy_time)
        text_box.send_keys(random.choice(potential_comments))
        time.sleep(sleepy_time)
        text_box.send_keys(Keys.ENTER)
        comment += 1
        print(f"{comment} Comment...")

    except:
        time.sleep(sleepy_time)
        print("Unable to comment on this photo...")

    finally:
        time.sleep(sleepy_time)

    return comment
