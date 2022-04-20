from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TweetsService:
    def __init__(self, driver):
        self.driver = driver

    def getTweets(self):
        tweets = self.driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')
        self.lastPosition = self.driver.execute_script("return window.pageYoffset;")
        return tweets

    def scrollDown(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1)
        self.currentPosition = self.driver.execute_script("return window.pageYOffset;")

    def getTweetData(self, tweet):
        user = tweet.find_element(By.XPATH, './/span').text
        comment = tweet.find_element(By.XPATH, './/div[2]/div[2]/div[2]/div[2]').text
        try:
            date = tweet.find_element(By.XPATH, './/time').get_attribute('datetime')
        except NoSuchElementException:
            return
        tweetData = (user, date, comment)
        return tweetData
