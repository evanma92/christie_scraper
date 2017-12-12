from selenium import webdriver
import time

path_to_chromedriver = '/Users/evanma/Downloads/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'http://www.sothebys.com/en/auctions/2017/contemporary-art-evening-auction-n09761.html#&page=all&sort=lotSortNum-asc&range=0|100&viewMode=list'
browser.get(url)

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

sothesby_links = []
for div in browser.find_elements_by_class_name("image"):
	sothesby_links.append(div.find_element_by_css_selector('a').get_attribute('href'))

# the last 6 elements with the class 'cta-image' are irrelevant
# sothesby_links = sothesby_links[:-6]

print(sothesby_links)

print(len(sothesby_links))

