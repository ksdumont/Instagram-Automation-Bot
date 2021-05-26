import itertools
from selenium import webdriver
from util.login import *
import csv
from datetime import datetime


def get_user_followers(browser, url, amount, user):
    global follower_index
    sleepy_time = 4
    followers = []
    total_follower_count = 0

    browser.get(url)
    time.sleep(sleepy_time)

    followers_button = browser.find_element_by_xpath("//a[contains(@href,'/followers')]")
    followers_button.click()
    time.sleep(sleepy_time)
    time.sleep(sleepy_time)

    followers_list = browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
    followers_list.click()
    time.sleep(sleepy_time)

    follower_css_selector = "ul div li:nth-child({}) a.notranslate"

    with open(f'../csv_files/{user}_followers.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=",")

        for group in itertools.count(start=1, step=12):
            if group > amount:
                break

            time.sleep(sleepy_time)

            for follower_index in range(group, group + 12):
                follower = browser.find_element_by_css_selector(follower_css_selector.format(follower_index)).text
                followers.append(follower)

                if len(followers) == 20:
                    writer.writerow(followers)
                    total_follower_count += 20
                    print(f"{total_follower_count} followers from {user}")
                    followers.clear()

            last_follower = browser.find_element_by_css_selector(follower_css_selector.format(follower_index))
            browser.execute_script("arguments[0].scrollIntoView();", last_follower)

    print(f"Created '{user}_followers.csv' and stored {total_follower_count} of {user}'s followers...")

    return followers


def main():
    start_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    user = input("Enter the user you would like to get followers from: ")
    amount = int(input("How many of their followers would you like to get? "))

    print("STARTING AT:      ", start_time)

    option = webdriver.ChromeOptions()

    # Removes navigator.webdriver flag

    # For older ChromeDriver under version 79.0.3945.16
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)

    # For ChromeDriver version 79.0.3945.16 or over
    option.add_argument('--disable-blink-features=AutomationControlled')

    browser = webdriver.Chrome(options=option)

    # Remove navigator.webdriver Flag using JavaScript
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    login(browser)

    print(f"Heading to {user}'s page...")

    get_user_followers(browser, f"https://www.instagram.com/{user}", amount, user)

    end_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    print("STARTED AT:      ", start_time)
    print("ENDING AT:      ", end_time)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
