from selenium import webdriver


opsi = webdriver.firefox.options.Options()
opsi.headless = False

binary = webdriver.firefox.firefox_binary.FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
cap['marionette'] = True
browser=webdriver.Firefox(options=opsi,capabilities=cap,firefox_binary=binary)
browser.get('https://tokoperhutani.com/')

pemberitahuan = browser.find_element_by_xpath('//*[@id="bannerModal"]/div/div/div[1]/button').click()
retail = browser.get('https://tokoperhutani.com/beranda')
login = browser.find_element_by_xpath('/html/body/div/nav/div/div[2]/ul/li[1]/a/strong').click()
email = browser.find_element_by_id('email').send_keys("yusniarnss29@gmail.com")
password = browser.find_element_by_id('password').send_keys("94A310")
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