# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from contact_name import ContactName
from contact_company import ContactCompany
from contact_address import ContactAddress
from contact_anniversary import ContactAnniversary
from contact_birthday import ContactBirthday
from contact_contacts import ContactContacts
from contact_extra_contacts import ContactExtraContacts
from contact_mobile import ContactMobile
from contact_work import ContactWork
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

    def new_contact_name(self, driver, contact_name):
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").send_keys(contact_name.firstname)
        driver.find_element(By.NAME, "middlename").click()
        driver.find_element(By.NAME, "middlename").send_keys(contact_name.middlename)
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").send_keys(contact_name.lastname)
        driver.find_element(By.NAME, "nickname").click()
        driver.find_element(By.NAME, "nickname").send_keys(contact_name.nickname)

    def new_contact_company(self, driver, contact_company):
        driver.find_element(By.NAME, "company").click()
        driver.find_element(By.NAME, "company").send_keys(contact_company.name_company)

    def new_contact_address(self, driver, contact_address):
        driver.find_element(By.NAME, "address").click()
        driver.find_element(By.NAME, "address").send_keys(contact_address.city)
        driver.find_element(By.NAME, "home").click()
        driver.find_element(By.NAME, "home").send_keys(contact_address.street)

    def new_contact_mobile(self, driver, contact_mobile):
        driver.find_element(By.NAME, "mobile").click()
        driver.find_element(By.NAME, "mobile").send_keys(contact_mobile.mobile_number)

    def new_contact_work(self, driver, contact_work):
        driver.find_element(By.NAME, "work").click()
        driver.find_element(By.NAME, "work").send_keys(contact_work.work_name)

    def new_contact_contacts(self, driver, contact_contacts):
        driver.find_element(By.NAME, "fax").click()
        driver.find_element(By.NAME, "fax").send_keys(contact_contacts.fax_method)
        driver.find_element(By.NAME, "email").click()
        driver.find_element(By.NAME, "email").send_keys(contact_contacts.first_email)
        driver.find_element(By.NAME, "email2").click()
        driver.find_element(By.NAME, "email2").send_keys(contact_contacts.second_email)
        driver.find_element(By.NAME, "email3").click()
        driver.find_element(By.NAME, "email3").send_keys(contact_contacts.third_email)
        driver.find_element(By.NAME, "homepage").click()
        driver.find_element(By.NAME, "homepage").send_keys(contact_contacts.homepage)

    def new_contact_birhday(self, driver, contact_birthday):
        driver.find_element(By.NAME, "bday").click()
        Select(driver.find_element(By.NAME, "bday")).select_by_visible_text(contact_birthday.bday)
        driver.find_element(By.NAME, "bmonth").click()
        Select(driver.find_element(By.NAME, "bmonth")).select_by_visible_text(contact_birthday.bmonth)
        driver.find_element(By.NAME, "byear").click()
        driver.find_element(By.NAME, "byear").send_keys(contact_birthday.byear)

    def new_contact_anniversary(self, driver, contact_anniversary):
        driver.find_element(By.NAME, "aday").click()
        Select(driver.find_element(By.NAME, "aday")).select_by_visible_text(contact_anniversary.aday)
        driver.find_element(By.NAME, "amonth").click()
        Select(driver.find_element(By.NAME, "amonth")).select_by_visible_text(contact_anniversary.amonth)
        driver.find_element(By.NAME, "ayear").click()
        driver.find_element(By.NAME, "ayear").send_keys(contact_anniversary.ayear)

    def new_contact_extra_contacts(self, driver, contact_extra_contacts):
        driver.find_element(By.NAME, "address2").click()
        driver.find_element(By.NAME, "address2").send_keys(contact_extra_contacts.extra_address)
        driver.find_element(By.NAME, "phone2").click()
        driver.find_element(By.NAME, "phone2").send_keys(contact_extra_contacts.extra_phone)
        driver.find_element(By.NAME, "notes").click()
        driver.find_element(By.NAME, "notes").send_keys(contact_extra_contacts.notes)

    def new_contact_create(self, driver):
        driver.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()

    def logout(self, driver):
        driver.find_element(By.LINK_TEXT, "home").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def test_contacts(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, "admin", "secret")
        self.new_contact_name(driver, ContactName("Artem", "AS", "Artemov", "artemka"))
        self.new_contact_company(driver, ContactCompany("Atom"))
        self.new_contact_address(driver, ContactAddress("Novosibirsk", "Lenina"))
        self.new_contact_mobile(driver, ContactMobile("3181818"))
        self.new_contact_work(driver, ContactWork("Staffcop"))
        self.new_contact_contacts(driver, ContactContacts("3431212", "artemio.kka", "artemio.kka1@gmail.com",
                                                          "artemio.kka2@gmail.com", "artemio"))
        self.new_contact_birhday(driver, ContactBirthday("8", "December", "1993"))
        self.new_contact_anniversary(driver, ContactAnniversary("17", "January", "1998"))
        self.new_contact_extra_contacts(driver, ContactExtraContacts("Address", "AddressHome", "Test"))
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
