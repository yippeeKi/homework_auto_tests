from selenium import webdriver
from selenium.webdriver.common.by import By
from test_add_group.fixture.group import GroupHelper
from test_add_group.fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def close(self):
        self.driver.quit()