from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = Service("/Users/faisalalnamlah/Desktop/Python Practice/chromedriver")
web_page = webdriver.Chrome(service=chrome_driver_path)

# url = 'https://en.wikipedia.org/wiki/Main_Page'
# url_1 = "http://secure-retreat-92358.herokuapp.com/"
# web_page.get(url_1)

# article_count = web_page.find_element(By.CSS_SELECTOR, '#articlecount a')
# article_count.click()

# clicking a link by its text:
# donate = web_page.find_element(By.LINK_TEXT, "Donate")
# donate.click()

# writing in inputs and pressing a key:
# search = web_page.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# Challenge:
# first_name = web_page.find_element(By.NAME, "fName")
# first_name.send_keys("Fai")
# last_name = web_page.find_element(By.NAME, "lName")
# last_name.send_keys("Moe")
# email = web_page.find_element(By.NAME, "email")
# email.send_keys("fai@hotmail.com")
# button = web_page.find_element(By.CLASS_NAME, "btn")
# button.click()
# time.sleep(100)

