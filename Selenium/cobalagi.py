# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:43:31 2019

@author: innal
"""

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
opsi = Options()
opsi.headless = False
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
cap = DesiredCapabilities().FIREFOX
cap['marionette'] = True
browser=Firefox(executable_path='geckodriver.exe',options=opsi,capabilities=cap,firefox_binary=binary)
browser.get('https://tokoperhutani.com/')
pemberitahuan = browser.find_element_by_xpath('//*[@id="bannerModal"]/div/div/div[1]/button').click()
retail = browser.get('https://tokoperhutani.com/beranda')
login = browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/li[1]/a/strong').click()
email = browser.find_element_by_id('email').send_keys("naomich07@gmail.com")
password = browser.find_element_by_id('password').send_keys("409566")
tombol = browser.find_element_by_class_name('le-button').click()
browser.find_element_by_link_text('Beranda').click()
retail = browser.get('https://tokoperhutani.com/beranda')
wilayah = browser.find_element_by_id('wilayah').click()
plh_wilayah = browser.find_element_by_xpath('//*[@id="wilayah"]/option[4]').click()
browser.implicitly_wait(5)
kota = browser.find_element_by_id('kota').click()
plh_kota = browser.find_element_by_xpath('//*[@id="kota"]/option[3]').click()
browser.implicitly_wait(5)
tpk = browser.find_element_by_id('select_kota').click()
plh_tpk = browser.find_element_by_xpath('//*[@id="select_kota"]/option[3]').click()
browser.implicitly_wait(5)
cari = browser.find_element_by_id('i_submit').click()