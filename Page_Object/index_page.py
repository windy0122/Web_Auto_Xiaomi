from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class IndexPage(object):
    def __init__(self, driver):
        self.driver = driver

    def is_user_info_exist(self):
        logout_button = "logoutLink"
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, logout_button)))
            return True
        except:
            return False



