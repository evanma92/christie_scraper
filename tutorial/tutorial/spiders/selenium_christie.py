from selenium import webdriver
import time

path_to_chromedriver = '/Users/evanma/Downloads/chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'http://www.christies.com/salelanding/index.aspx?intsaleid=26796&saletitle='
browser.get(url)

# ensures that all the lots are loaded
load_all = browser.find_element_by_css_selector("a.load-all")
browser.execute_script("arguments[0].click();", load_all)

# lets the browser sleep so that it gives time to get all the lots
time.sleep(10)

required_links = []

# the required lots are discovered through the tag 'a' with class 'cta-image'
for a in browser.find_elements_by_css_selector("a.cta-image"):
	required_links.append(a.get_attribute('href'))

# the last 6 elements with the class 'cta-image' are irrelevant
required_links = required_links[:-6]

print(len(required_links))

