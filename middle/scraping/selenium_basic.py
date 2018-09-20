from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/honest/chromedriver')
driver.fullscreen_window()
driver.get('https://dnf.qq.com')
driver.find_element_by_class_name('gw').click()
driver.find_element_by_class_name('recharge').click()

driver.switch_to_window(driver.window_handles[1])
driver.find_element_by_class_name('z').click()

driver.switch_to_window(driver.window_handles[2])
driver.switch_to_frame('login_frame')
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('1131328108')
driver.find_element_by_id('p').send_keys('woainixll10')
driver.find_element_by_id('login_button').click()
