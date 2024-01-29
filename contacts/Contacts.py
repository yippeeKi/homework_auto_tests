# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class Contacts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/edit.php")

    def login(self, driver, username, password):
        driver.find_element(By.NAME, "user").send_keys(username)
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def new_contact_name(self, driver):
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").send_keys("Artem")
        driver.find_element(By.NAME, "middlename").click()
        driver.find_element(By.NAME, "middlename").send_keys("AS")
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").send_keys("Artemov")
        driver.find_element(By.NAME, "nickname").click()
        driver.find_element(By.NAME, "nickname").send_keys("artemka")

    def new_contact_company(self, driver):
        driver.find_element(By.NAME, "company").click()
        driver.find_element(By.NAME, "company").send_keys("Atom")

    def new_contact_address(self, driver):
        driver.find_element(By.NAME, "address").click()
        driver.find_element(By.NAME, "address").send_keys("Novosibirsk")
        driver.find_element(By.NAME, "home").click()
        driver.find_element(By.NAME, "home").send_keys("Lenina")

    def new_contact_mobile(self, driver):
        driver.find_element(By.NAME, "mobile").click()
        driver.find_element(By.NAME, "mobile").send_keys("3434343")

    def new_contact_work(self, driver):
        driver.find_element(By.NAME, "work").click()
        driver.find_element(By.NAME, "work").send_keys("Staffcop")

    def new_contact_contacts(self, driver):
        driver.find_element(By.NAME, "fax").click()
        driver.find_element(By.NAME, "fax").send_keys("3431212")
        driver.find_element(By.NAME, "email").click()
        driver.find_element(By.NAME, "email").send_keys("artemio.kka@gmail.com")
        driver.find_element(By.NAME, "email").click()
        driver.find_element(By.NAME, "email2").click()
        driver.find_element(By.NAME, "email2").send_keys("artemio.kka1@gmail.com")
        driver.find_element(By.NAME, "email3").click()
        driver.find_element(By.NAME, "email3").send_keys("artemio.kka2@gmail.com")
        driver.find_element(By.NAME, "homepage").click()
        driver.find_element(By.NAME, "homepage").send_keys("artemio")

    def new_contact_birhday(self, driver):
        driver.find_element(By.NAME, "bday").click()
        Select(driver.find_element(By.NAME, "bday")).select_by_visible_text("8")
        driver.find_element(By.NAME, "bmonth").click()
        Select(driver.find_element(By.NAME, "bmonth")).select_by_visible_text("December")
        driver.find_element(By.NAME, "byear").click()
        driver.find_element(By.NAME, "byear").send_keys("1993")

    def new_contact_anniversary(self, driver):
        driver.find_element(By.NAME, "aday").click()
        Select(driver.find_element(By.NAME, "aday")).select_by_visible_text("17")
        driver.find_element(By.NAME, "amonth").click()
        Select(driver.find_element(By.NAME, "amonth")).select_by_visible_text("January")
        driver.find_element(By.NAME, "ayear").click()
        driver.find_element(By.NAME, "ayear").send_keys("1998")

    def new_contact_extra_contacts(self, driver):
        driver.find_element(By.NAME, "address2").click()
        driver.find_element(By.NAME, "address2").send_keys("Address")
        driver.find_element(By.NAME, "phone2").click()
        driver.find_element(By.NAME, "phone2").send_keys("AddressHome")
        driver.find_element(By.NAME, "notes").click()
        driver.find_element(By.NAME, "notes").send_keys("Test")

    def new_contact_create(self, driver):
        driver.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()

    def logout(self, driver):
        driver.find_element(By.LINK_TEXT, "home").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def test_contacts(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, "admin", "secret")
        self.new_contact_name(driver)
        self.new_contact_company(driver)
        self.new_contact_address(driver)
        self.new_contact_work(driver)
        self.new_contact_contacts(driver)
        self.new_contact_birhday(driver)
        self.new_contact_anniversary(driver)
        self.new_contact_extra_contacts(driver)
        self.new_contact_create(driver)
        self.open_home_page(driver)
        self.logout(driver)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
