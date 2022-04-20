from webbrowser import Chrome
from selenium.webdriver import Chrome


class DriverConfigurator:
    def __init__(self, path):
        self.path = path
        self.driver = Chrome(self.path)
        self.driver.maximize_window()

    def OpenDriver(self):
        return self.driver
