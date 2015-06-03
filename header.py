# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

links_landing_titles = {
    "Resources" : r"Sauce Resources",
    "Pricing" : r"Sauce Labs: Pricing",
    "Features" : r"Sauce Labs: Features",
    "Docs" : r"Sauce Labs Docs",
    "Sign up" : r"Sauce Labs: Sign Up for a Free Trial",
    "Company" : r"Sauce Labs: Values",
    "Enterprise" : r"Sauce Labs: Enterprise-grade testing on Sauce",
    "Log in" : r"Sauce Labs: Login",
    "Community" : r"Open Sauce",
    "Solutions" : r"Selenium Testing by Sauce Labs",
    }

class SauceLabsHeaders(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/"
        self.verificationErrors = []

    def test_sauce_labs_headers(self):
        driver = self.driver

        for link in links_landing_titles:
            driver.get(self.base_url)
            driver.find_element_by_css_selector(".hamburger").click();
            driver.find_element_by_css_selector("a[title='"+link+"']").click()
            expected_title = links_landing_titles[link]
            try: self.assertRegexpMatches(driver.title, expected_title)
            except AssertionError as e: self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
