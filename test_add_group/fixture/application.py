from selenium import webdriver
from selenium.webdriver.common.by import By
from test_add_group.fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def open_group_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        driver = self.driver
        self.open_group_page()
        # init new group
        driver.find_element(By.NAME, "new").click()
        # add new group
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").clear()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").clear()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element(By.NAME, "submit").click()
        self.return_to_groups()

    def return_to_groups(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def close(self):
        self.driver.quit()