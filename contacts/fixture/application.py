from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from contacts.fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/edit.php")

    def new_contact_name(self, contact_name):
        driver = self.driver
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").send_keys(contact_name.firstname)
        driver.find_element(By.NAME, "middlename").click()
        driver.find_element(By.NAME, "middlename").send_keys(contact_name.middlename)
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").send_keys(contact_name.lastname)
        driver.find_element(By.NAME, "nickname").click()
        driver.find_element(By.NAME, "nickname").send_keys(contact_name.nickname)

    def new_contact_company(self, contact_company):
        driver = self.driver
        driver.find_element(By.NAME, "company").click()
        driver.find_element(By.NAME, "company").send_keys(contact_company.name_company)

    def new_contact_address(self, contact_address):
        driver = self.driver
        driver.find_element(By.NAME, "address").click()
        driver.find_element(By.NAME, "address").send_keys(contact_address.city)
        driver.find_element(By.NAME, "home").click()
        driver.find_element(By.NAME, "home").send_keys(contact_address.street)

    def new_contact_mobile(self, contact_mobile):
        driver = self.driver
        driver.find_element(By.NAME, "mobile").click()
        driver.find_element(By.NAME, "mobile").send_keys(contact_mobile.mobile_number)

    def new_contact_work(self, contact_work):
        driver = self.driver
        driver.find_element(By.NAME, "work").click()
        driver.find_element(By.NAME, "work").send_keys(contact_work.work_name)

    def new_contact_contacts(self, contact_contacts):
        driver = self.driver
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

    def new_contact_birhday(self, contact_birthday):
        driver = self.driver
        driver.find_element(By.NAME, "bday").click()
        Select(driver.find_element(By.NAME, "bday")).select_by_visible_text(contact_birthday.bday)
        driver.find_element(By.NAME, "bmonth").click()
        Select(driver.find_element(By.NAME, "bmonth")).select_by_visible_text(contact_birthday.bmonth)
        driver.find_element(By.NAME, "byear").click()
        driver.find_element(By.NAME, "byear").send_keys(contact_birthday.byear)

    def new_contact_anniversary(self, contact_anniversary):
        driver = self.driver
        driver.find_element(By.NAME, "aday").click()
        Select(driver.find_element(By.NAME, "aday")).select_by_visible_text(contact_anniversary.aday)
        driver.find_element(By.NAME, "amonth").click()
        Select(driver.find_element(By.NAME, "amonth")).select_by_visible_text(contact_anniversary.amonth)
        driver.find_element(By.NAME, "ayear").click()
        driver.find_element(By.NAME, "ayear").send_keys(contact_anniversary.ayear)

    def new_contact_extra_contacts(self, contact_extra_contacts):
        driver = self.driver
        driver.find_element(By.NAME, "address2").click()
        driver.find_element(By.NAME, "address2").send_keys(contact_extra_contacts.extra_address)
        driver.find_element(By.NAME, "phone2").click()
        driver.find_element(By.NAME, "phone2").send_keys(contact_extra_contacts.extra_phone)
        driver.find_element(By.NAME, "notes").click()
        driver.find_element(By.NAME, "notes").send_keys(contact_extra_contacts.notes)

    def new_contact_create(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.new_contact_create()
        self.open_home_page()

    def close(self):
        self.driver.quit()
