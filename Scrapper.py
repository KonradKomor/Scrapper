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
    def logInToTwitter(self):
        driver = Chrome(self.path)
        driver.maximize_window()
        driver.get('https://www.twitter.com/login')
        time.sleep(2)
        mailInput = driver.find_element(By.XPATH, self.emailInputXpath)
        mailInput.send_keys(self.mail)
        nextButtonInput=driver.find_element(By.XPATH,self.nextButtonXpath)
        nextButtonInput.click()
        time.sleep(2)
        accountValidatorInput=driver.find_element(By.XPATH,self.accountValidatorXpath)
        accountValidatorInput.send_keys(self.username)
        self.nextButtonXpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div'
        nextButtonInput=driver.find_element(By.XPATH,self.nextButtonXpath)
        nextButtonInput.click()
        time.sleep(2)
        passwordInput = driver.find_element(By.XPATH, self.passwordButtonXpath)
        passwordInput.send_keys(self.password)
        time.sleep(2)
        self.nextButtonXpath='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span/span'
        nextButtonInput=driver.find_element(By.XPATH,self.nextButtonXpath)
        nextButtonInput.click()
