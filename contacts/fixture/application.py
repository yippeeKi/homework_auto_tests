from selenium import webdriver 
from contacts.fixture.contacts import ContactsHelper
from contacts.fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.contacts = ContactsHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/edit.php")

    def close(self):
        self.driver.quit()
