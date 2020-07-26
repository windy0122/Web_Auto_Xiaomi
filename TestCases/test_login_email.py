import pytest
from TestDatas import login_datas as ld
from Page_Object.index_page import IndexPage
from TestDatas.common_datas import login_url
from Page_Object.login_page import LoginPage
from selenium import webdriver
import unittest
from ddt import ddt, data


# @ddt
# class TestLogin(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print('===========测试开始===========')
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get(login_url)
    #     cls.driver.maximize_window()
    #     cls.lg = LoginPage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #
    # def tearDown(self):
    #     self.driver.refresh()
    #
    # @data(*ld.login_data)
    # def test_login_0_error_ddt(self, datas):
    #     self.lg.login(datas['username'], datas['password'])
    #     self.assertEqual(self.lg.get_error_msg(), datas['check'])

@pytest.mark.usefixtures('access_web')
@pytest.mark.usefixtures('refresh_page')
class TestLogin(object):

    # 异常用例
    @pytest.mark.parametrize('data', ld.login_data)
    def test_login_0_error(self, data, access_web):
        access_web[1].login(data['username'], data['password'])
        assert access_web[1].get_error_msg(), data['check']

    # 正常登陆用例
    def test_login_1_success(self, access_web):
        access_web[1].login(ld.success_data['username'], ld.success_data['password'])
        assert IndexPage(access_web[0]).is_user_info_exist()








