'''
    自动以测试框架类
'''
from selenium import webdriver
from .driver import browser
import os
import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
