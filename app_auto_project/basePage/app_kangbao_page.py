__author__ = 'lenovo'
from app_auto_project.basePage.app_base import AppBase
from selenium.webdriver.common.by import By
import time


class Kangbao(AppBase):
    # 用户名
    username = (By.XPATH, "//android.widget.EditText[@text='请输入手机号']")
    password = (By.XPATH, "//android.widget.EditText[@text='请输入4位验证码']")
    loginButton = (By.XPATH, "//android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup[1]")

    def login(self, telephone, telMima):
        self.send_keys(self.username, telephone)
        time.sleep(3)
        self.send_keys(self.password, telMima)
        self.click(self.loginButton)








