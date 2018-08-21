__author__ = 'lenovo'
from app_auto_project.basePage import app_kangbao_page
import unittest
from appium import webdriver


class TestKangbao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.desird_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': 'P4M7N15425007120',
            'appPackage': 'com.ijourney.conbow',
            'appActivity': 'com.ijourney.conbow.MainActivity',
            'noReset': 'True'
        }
        cls.appiumDriver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cls.desird_caps)

    def test01(self):
        # 登录慷宝app
        self.appiumDriver.implicitly_wait(5)
        app = app_kangbao_page.Kangbao(self.appiumDriver)
        app.login("17310520712", '3838')

    @classmethod
    def tearDownClass(cls):
        cls.appiumDriver.quit()







