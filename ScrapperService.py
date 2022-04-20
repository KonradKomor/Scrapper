from getpass import getpass
from time import sleep
from DriverConfigurator import DriverConfigurator
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
import time


class ScrapperService:
    emailInputXpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input'
    nextButtonXpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span'
    passwordButtonXpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'

    def __init__(self, mail, password, username, driver):
        self.mail = mail
        self.password = password
        self.username = username
        self.accountValidatorXpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
        self.driver = driver
        self.lastPosition = set()
        self.currentPosition = set()

    def logInToTwitter(self):
        self.driver.get('https://www.twitter.com/login')
        nextButtonXpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span'
        time.sleep(2)
        mailInput = self.driver.find_element(By.XPATH, self.emailInputXpath)
        mailInput.send_keys(self.mail)
        nextButtonInput = self.driver.find_element(By.XPATH, nextButtonXpath)
        nextButtonInput.click()
        time.sleep(2)
        accountValidatorInput = self.driver.find_element(By.XPATH, self.accountValidatorXpath)
        accountValidatorInput.send_keys(self.username)
        nextButtonXpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div'
        nextButtonInput = self.driver.find_element(By.XPATH, nextButtonXpath)
        nextButtonInput.click()
        time.sleep(2)
        passwordInput = self.driver.find_element(By.XPATH, self.passwordButtonXpath)
        passwordInput.send_keys(self.password)
        time.sleep(2)
        nextButtonXpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span/span'
        nextButtonInput = self.driver.find_element(By.XPATH, nextButtonXpath)
        nextButtonInput.click()

    def findPostsAboutTopic(self, topic):
        time.sleep(2)
        searchBarXpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'
        searchBarInput = self.driver.find_element(By.XPATH, searchBarXpath)
        searchBarInput.send_keys(topic)
        searchBarInput.send_keys(Keys.RETURN)
        sleep(2)
        latestXpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div/span'
        self.driver.find_element(By.XPATH, latestXpath).click()
        return self.driver
