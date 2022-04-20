from getpass import getpass
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
import time
class Scrapper:
    def __init__(self,mail,password,path,username):
        self.mail = mail
        self.password = password
        self.path = path
        self.username = username
        self.emailInputXpath= '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input'
        self.accountValidatorXpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
        self.nextButtonXpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span'
        self.passwordButtonXpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
        self.driver = Chrome(self.path)
        self.driver.maximize_window()
        self.driver.get('https://www.twitter.com/login')
        self.lastPosition=set()
        self.currentPosition=set()
    def logInToTwitter(self):
        time.sleep(2)
        mailInput = self.driver.find_element(By.XPATH, self.emailInputXpath)
        mailInput.send_keys(self.mail)
        nextButtonInput=self.driver.find_element(By.XPATH,self.nextButtonXpath)
        nextButtonInput.click()
        time.sleep(2)
        accountValidatorInput=self.driver.find_element(By.XPATH,self.accountValidatorXpath)
        accountValidatorInput.send_keys(self.username)
        self.nextButtonXpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div'
        nextButtonInput=self.driver.find_element(By.XPATH,self.nextButtonXpath)
        nextButtonInput.click()
        time.sleep(2)
        passwordInput = self.driver.find_element(By.XPATH, self.passwordButtonXpath)
        passwordInput.send_keys(self.password)
        time.sleep(2)
        self.nextButtonXpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span/span'
        nextButtonInput=self.driver.find_element(By.XPATH,self.nextButtonXpath)
        nextButtonInput.click()
    def findPostsAboutTopic(self):
            time.sleep(2)
            searchBarXpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'
            searchBarInput = self.driver.find_element(By.XPATH,searchBarXpath)
            searchBarInput.send_keys("polski ład")
            searchBarInput.send_keys(Keys.RETURN)
            sleep(2)
            latestXpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div/span'
            self.driver.find_element(By.XPATH, latestXpath).click()
    def getTweets(self):
        tweets = self.driver.find_elements(By.XPATH,'//article[@data-testid="tweet"]')
        self.lastPosition=self.driver.execute_script("return window.pageYoffset;")
        return tweets
    def scrollDown(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(1)
        self.currentPosition=self.driver.execute_script("return window.pageYOffset;")