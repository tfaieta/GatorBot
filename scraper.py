import time
from selenium import webdriver

# The URL we want to browse to
urls = [
    "https://www.reddit.com/r/ufl",
    "https://www.facebook.com/groups/124944151183714/"
]

# Loop through URLS
for url in urls:
    driver = webdriver.Firefox()
    driver.get(url)
    driver.execute_script("window.scrollTo(0,1000);")
    time.sleep(5)

