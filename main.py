# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

from Scrapper import Scrapper


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """driver.get('https://www.twitter.com/login')
    search = driver.find_element_by_name("username")
    search.send_keys(mail)
    Next = driver.find_element_by_xpath("//span[.='Dalej']")
    Next.click()
    password = driver.find_element_by_xpath('//input[@name="session[password]"]')
    password.send_keys(twitterPassword)
    password.send_keys(Keys.RETURN)
    search_input = driver.find_element_by_xpath('//input[@aria-label="Search query"]')
    search_input.send_keys('#polskiład')
    search_input.send_keys(Keys.RETURN)
    driver.find_element_by_link_text('Latest').click()
    cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
    card = cards[0]
    card.find_element_by_xpath('./div[2]/div[1]//span').text
    # twitter handle
    card.find_element_by_xpath('.//span[contains(text(), "@")]').text
    card.find_element_by_xpath('.//time').get_attribute('datetime')
    card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
    card.find_element_by_xpath('.//div[@data-testid="reply"]'). """

    scrapper = Scrapper("komor.konrad0@gmail.com", "TwitterScraper", "C:/Users/konra/chromedriver.exe","@Konrad38611406")
    scrapper.logInToTwitter()
    scrapper.findPostsAboutTopic()
