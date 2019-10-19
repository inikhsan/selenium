# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#print("Masukkan Npm Anda:")
#npm = input()
#print("Masukkan Password SIAP Anda:")
#paswd = input('')

opsi = Options()

opsi.headless = False
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
cap = DesiredCapabilities().FIREFOX
cap['marionette'] = True

browser=Firefox(executable_path='geckodriver.exe',
options=opsi,capabilities=cap,firefox_binary=binary)
browser.get('https://www.youtube.com')
browser.find_element_by_name('search_query').send_keys('mundur maju')
browser.find_element_by_id('search-icon-legacy').click()
browser.get('https://www.youtube.com/watch?v=zCmHodTpt9I')

#name = browser.find_element_by_name('user_name')
#word = browser.find_element_by_name('user_pass')
#login = browser.find_element_by_name('login')

#name.send_keys(npm)
#word.send_keys(paswd)
#login.click()