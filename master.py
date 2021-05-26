from selenium import webdriver
from util.login import *
from util.tags import *
from follow_scripts.follow_users import follow_users
from follow_scripts.unfollow_users import unfollow_users
from like_comment_scripts.like_by_tags import visit_tag
from datetime import datetime
import random


def main():
    session_likes = int(input("How many photos do you want to like this session?"))

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

    tags = primary_yoga_tags
    random.shuffle(tags)

    start = 0
    end = 5

    iteration_count = 0

    script_running = True

    users_followed = 0
    unfollowed = 0
    total_likes = 0
    total_comments = 0

    s1 = random.randint(200, 300)
    s2 = random.randint(200, 300)
    s3 = random.randint(200, 300)
    s4 = random.randint(8, 12)

    start_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print("STARTING AT:      ", start_time)

    while script_running:
        curr_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        iteration_count += 1
        print("Iteration: ", iteration_count)
        print(curr_time)

        # users_followed += len(follow_users(browser, './csv_files/yogaasanatutorial_followers.csv'))
        # print(f"You have followed {users_followed} users so far...")
        #
        # print(f"sleeping for {s1} seconds...")
        # time.sleep(s1)

        for tag in tags[start:end]:
            print("-------- V I S I T I N G  #" + tag + " --------")
            curr_likes = visit_tag(browser, f"https://www.instagram.com/explore/tags/{tag}")
            total_likes += curr_likes
            print(f"You have liked {total_likes} photos so far...")
            print(f"You have left {total_comments} comments so far...")
            time.sleep(s4)

        # print(f"sleeping for {s2} seconds...")
        # time.sleep(s2)
        #
        # unfollowed += len(unfollow_users(browser, './csv_files/followed.csv'))
        # print(f"You have unfollowed {unfollowed} users so far...")

        start += 5
        end += 5

        if total_likes > session_likes:
            script_running = False

        print(f"sleeping for {s3} seconds...")
        time.sleep(s3)

    end_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    print("- - - - - - - - - - - - - - - - - - - - - - - - -")
    print("STARTED AT:      ", start_time)
    print("ENDED AT:      ", end_time)
    print(f"{iteration_count} iterations...")
    print(f"You have followed {users_followed} users today...")
    print(f"You have unfollowed {unfollowed} users today...")
    print(f"You have liked {total_likes} photos today...")
    print(f"You have left {total_comments} comments today...")
    print("- - - - - - - - - - - - - - - - - - - - - - - - -")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

