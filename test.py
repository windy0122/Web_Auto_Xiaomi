from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://mail.163.com/')
driver.maximize_window()
time.sleep(2)

try:
    driver.find_element_by_name("email").send_keys('windy_wudi')
    driver.find_element_by_xpath("//input[@name='password']").send_keys('wudi19920122')

    time.sleep(4)
except:
    driver.quit()



