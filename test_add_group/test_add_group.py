# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
from application import Application
import unittest

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_app_dynamics_job(self):
        self.app.login("admin", "secret")
        self.app.create_group(Group("test name", "group name", "some"))
        self.app.logout()


    def is_element_present(self, how, what):
        try:
            self.app.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.app.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.app.close()

if __name__ == "__main__":
    unittest.main()
