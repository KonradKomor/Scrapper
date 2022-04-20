from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Tweets:
    def __init__(self,tweets):
        self.tweetsList=tweets
    def getTweetData(self,tweet):
        user = tweet.find_element(By.XPATH, './/span').text
        comment = tweet.find_element(By.XPATH, './/div[2]/div[2]/div[2]/div[2]').text
        try:
            date = tweet.find_element(By.XPATH, './/time').get_attribute('datetime')
        except NoSuchElementException:
            return
        tweetData = (user, date, comment)
        return tweetData