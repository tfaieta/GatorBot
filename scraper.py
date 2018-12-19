import time
import pathlib
from selenium import webdriver


def scrapeReddit(url):
    driver = webdriver.Firefox()
    driver.get(url)
    SCROLL_PAUSE_TIME = 4.0

    # Get tag names
    redditPostTitles = driver.find_elements_by_tag_name("H2")
    redditPostParagraphs = driver.find_elements_by_tag_name("P")

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

        for redditPostTitle in redditPostTitles:
            print(redditPostTitle.text)

        for redditPostParagraph in redditPostParagraphs:
            print(redditPostParagraph.text)


# MAIN

# The URL we want to browse to
urls = [
    "https://www.reddit.com/r/ufl",
    # "https://www.facebook.com/groups/124944151183714/"
]

reddit_data_folder = "./reddit_data/"
pathlib.Path(reddit_data_folder).mkdir(parents=True, exist_ok=True)

for url in urls:
    scrapeReddit(url)





