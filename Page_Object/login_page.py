# 此页面只管理页面操作

from PageLocators.login_locators import LoginPageLocators as loc
from Common.base_page import BasePage
import time


class LoginPage(BasePage):

    # 登录
    def login(self, username, password):
        doc = '登录页面_登录功能'
        self.click_ele(loc.login_button)
        self.send_keys_ele(loc.login_username, username, doc)
        self.send_keys_ele(loc.login_passwd, password, doc)

        self.click_ele(loc.login_button, doc)

    # 获取错误提示文案
    def get_error_msg(self):
        doc = '登录页面_错误提示信息'
        self.wait_eleVisible(loc.error_msg, doc=doc)
        return self.get_ele_text(loc.error_msg, doc)


