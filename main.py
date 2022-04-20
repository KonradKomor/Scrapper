# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

from ScrapperService import ScrapperService
from DriverConfigurator import DriverConfigurator
from TweetsService import TweetsService


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tweetDataList = []
    tweetIds = set()
    driver = DriverConfigurator("C:/Users/konra/chromedriver.exe")
    driver = driver.OpenDriver()
    scrapper = ScrapperService("komor.konrad0@gmail.com", "TwitterScraper", "@Konrad38611406", driver)
    scrapper.logInToTwitter()
    driver=scrapper.findPostsAboutTopic("Polski ład")
    while True:
        tweets = TweetsService(driver)
        for tweet in tweets.getTweets():
            data = tweets.getTweetData(tweet)
            if data:
                tweetId = ''.join(data)
                if tweetId not in tweetIds:
                    tweetIds.add(tweetId)
                    tweetDataList.append(data)
        tweets.scrollDown()
        if len(tweetDataList) > 20:
            break
    with open('tweets.csv', 'w', newline='', encoding='UTF-8') as f:
        header = ['Username', 'Timestamp', 'Text']
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(tweetDataList)
