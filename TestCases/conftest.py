import pytest
from selenium import webdriver
from Page_Object.login_page import LoginPage
from TestDatas import common_datas as cd
import time


driver = None


@pytest.fixture(scope='class')
def access_web():
    global driver
    # 前置操作
    print('===========测试用例执行之前，setup整个测试类执行一次===========')
    driver = webdriver.Chrome()
    driver.get(cd.login_url)
    driver.maximize_window()
    lg = LoginPage(driver)
    yield (driver, lg)
    # 后置操作
    print('===========测试用例执行之后，teardown整个测试类执行一次===========')
    driver.quit()


@pytest.fixture()
def refresh_page():
    global driver
    yield
    time.sleep(5)
    driver.refresh()
