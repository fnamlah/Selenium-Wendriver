from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_path = Service("/Users/faisalalnamlah/Desktop/Python Practice/chromedriver")
web_page = webdriver.Chrome(service=chrome_driver_path)
url = "https://www.python.org/"
web_page.get(url)

# event_time = web_page.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time')
# print(event_time.text)

events = {}
for number in range(1, 6):
    event_time = web_page.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{number}]/time').text
    event_title = web_page.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{number}]/a').text
    events.update({
        number: {
            'name': event_title,
            "data": event_time
        }
    })
    # print(event_time)
    # print(event_title)

print(events)
