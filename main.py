from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_path = Service("/Users/faisalalnamlah/Desktop/Python Practice/chromedriver")
web_page = webdriver.Chrome(service=chrome_driver_path)
url_1 = "https://www.python.org/"
url_2 = "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ?th=1"
web_page.get(url_2)

# getting price
# price_whole = web_page.find_element(By.CLASS_NAME, "a-price-whole").text
# price_fraction = web_page.find_element(By.CLASS_NAME, "a-price-fraction").text
# print(f"{price_whole}.{price_fraction}")


# Search Bar
# search_bar = web_page.find_element(By.NAME, "q")
# print(f"\n--Search Bar--")
# print(search_bar)
# print(search_bar.tag_name)
# print(f"{(search_bar.get_attribute('placeholder'))}\n")
# price = web_page.find_element(By.XPATH, '//*[@id="corePrice_feature_div"]/div/span/span[2]/span[2]').text
# print(price)

# Python Logo
# print("--Logo--")
# logo = web_page.find_element(By.CLASS_NAME, "python-logo")
# print(logo.tag_name)
# print(logo.get_attribute("alt"))
# print(f"{logo.size}\n")

# CSS Selector
# print("--CSS Selector--")
# css_link = web_page.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(f"{css_link.text}\n")


# Find by XPATH
# print("--XPATH--")
# bug_link = web_page.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(f"{bug_link.text}\n")



# closing the tab
web_page.close()
# closing the entire browser
# driver.quit()
