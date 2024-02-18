from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        driver = self.app.driver
        self.open_group_page()
        # init new group
        driver.find_element(By.NAME, "new").click()
        # add new group
        self.fill_group_form(group)
        # submit group creation
        driver.find_element(By.NAME, "submit").click()
        self.return_to_groups()

    def fill_group_form(self, group):
        driver = self.app.driver
        self.type("group_name", group.name)
        self.type("group_header", group.name)
        self.type("group_footer", group.name)

    def type(self, field_name, text):

        driver = self.app.driver
        if text.name is not None:
            driver.find_element(By.NAME(field_name)).click()
            driver.find_element(By.NAME(field_name)).clear()
            driver.find_element(By.NAME(field_name)).send_keys(text.name)

    def return_to_groups(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_page()
        self.select_first_group()
        driver.find_element(By.NAME, "delete").click()
        self.return_to_groups()

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()

    def modify_first_group(self, new_group_data):
        driver = self.app.driver
        self.open_group_page()
        self.select_first_group()
        driver.find_element(By.NAME, "edit").click()
        driver.find_element(By.NAME, "update").click()
        self.fill_group_form(new_group_data)
        self.return_to_groups()






