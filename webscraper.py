from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import csv

# THIS SCRAPER IS FOR EDUCATIONAL PURPOSES ONLY
# This web scraper goes to www.stockx.com and gathers information about my favorite shoe, Air Jordan 1s
# For each shoe, there is information such as model name, retail price, release date, etc.
# This program pulls data from the page and is then stored into a .csv file.

browser = webdriver.Chrome()

browser.get("https://stockx.com/")
print(browser.title)
print("-" * 25)

search = browser.find_element_by_name("q")
search.send_keys("Air Jordan 1")
search.send_keys(Keys.RETURN)

time.sleep(5)

# 10 shoes I want to scrape info from
shoes_url = ["https://stockx.com/air-jordan-1-retro-high-dark-mocha?size=10.5",
             "https://stockx.com/air-jordan-1-retro-high-light-smoke-grey?size=10.5",
             "https://stockx.com/air-jordan-1-retro-high-pine-green-black?size=10.5",
             "https://stockx.com/air-jordan-1-retro-high-black-game-royal?size=10.5",
             "https://stockx.com/air-jordan-1-retro-high-shattered-backboard-3?size=10.5",
             "https://stockx.com/air-jordan-1-retro-high-unc-leather?size=10.5",
             "https://stockx.com/air-jordan-1-retro-high-black-hyper-pink?size=10.5",
             "https://stockx.com/air-jordan-1-retro-high-shadow-2018?size=10.5",
             "https://stockx.com/air-jordan-1-retro-high-bred-toe?size=10.5",
             "https://stockx.com/air-jordan-1-retro-high-court-purple-white?size=10.5"]

# creation of the .csv file
csv_file = open('stockx henry jordan 1.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['Colorway', ' Retail price', ' Average sale price'])

def sneakersInfo():
    # method to get name of shoe and average sale price of shoe
    time.sleep(3)

    shoe_name = browser.find_element_by_xpath('//h1[@class="name"]').text
    # prints name of shoe
    print(shoe_name)

    shoe_retail_price = browser.find_element_by_xpath('//div[@class="detail"][3]/span').text
    # prints shoe retail price
    print("Retail price: " + shoe_retail_price)

    average_sale_price = browser.find_element_by_xpath('.//div[@class="gauge-container"][3]//div[@class="gauge-value"]').text
    print("Average sale price: " + average_sale_price)

    print("-" * 25)

    # writing collected data into a .csv file
    storeSneakerData = {}

    storeSneakerData['Model'] = shoe_name
    storeSneakerData['Retail_Price'] = " " + shoe_retail_price
    storeSneakerData['Avg_Sale_Price'] = " " + average_sale_price
    writer.writerow(storeSneakerData.values())

try:
    # runs method through each url in the list

    for each_url in shoes_url:
        browser.get(each_url)
        sneakersInfo()

except Exception as e:
    print(e)
    csv_file.close()
    browser.close()

