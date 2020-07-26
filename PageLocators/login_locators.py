from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    # 用户名输入框
    login_username = (By.ID, "username")
    # 密码输入框
    login_passwd = (By.ID, "pwd")
    # 登录按钮
    login_button = (By.ID, "login-button")
    # # 免登录密码框
    # un_login_button = (By.XPATH, "/html//input[@id='un-login']")
    # 错误提示
    error_msg = (By.XPATH, "//*[@id='login-main-form']/div/div[@class='err_tip']/div/span")





