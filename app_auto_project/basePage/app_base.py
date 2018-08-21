__author__ = 'lenovo'
from app_auto_project.public.log_app import Logger


class AppBase():
    def __init__(self, appium_driver):
        self.driver = appium_driver
        self.path = 'C:\\Users\\lenovo\\PycharmProjects\\untitled1\\app_auto_project\\logs' + '\\kangbao.log'
        self.lg = Logger(self.path)

    def find_element(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except:
            self.lg.error("没有找到元素%s" % str(loc))


    def send_keys(self, loc, txt):  # 输入方法
        try:
            return self.find_element(*loc).send_keys(txt)
        except:
            self.lg.error("输入%s失败！" % txt)

    def click(self, loc):  # 点击方法
        try:
            return self.find_element(*loc).click()
        except:
            self.lg.error("点击%s失败！" % str(loc))












