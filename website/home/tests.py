import os
import geckodriver_autoinstaller

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class HomePageTestCase(TestCase):
    def setUp(self):
        """Setup selenium."""
        geckodriver_autoinstaller.install()
        options = Options()
        options.headless = True if os.environ.get("HEADLESS") != "False" else False
        self.driver = webdriver.Firefox(options=options)
        host = os.environ["HOST"]
        port = os.environ["PORT"]
        self.url = f"{host}:{port}"

    def test_home_page_loads(self):
        """Animals that can speak are correctly identified"""
        self.driver.get(self.url)
        icon = self.driver.find_element_by_id("theme-img")
        icon.click()
        assert True
