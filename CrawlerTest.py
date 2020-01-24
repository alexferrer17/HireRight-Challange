from selenium import webdriver

import time

browser = webdriver.Chrome()
browser.get('https://wcca.wicourts.gov/case.html')
time.sleep(1)

#Last Name
lName = browser.find_element_by_name('lastName')
lName.send_keys("Smith")

#First Name
fName = browser.find_element_by_name('firstName')
fName.send_keys("John")

browser.find_element_by_name('search').click()
time.sleep(1)

search = browser.find_elements_by_class_name('case-link')
search[0].click()

browser.save_screenshot('screenshot.png')
