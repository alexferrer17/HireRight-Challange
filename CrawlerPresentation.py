from selenium import webdriver

import time

#User Input
lastName = raw_input("Enter The Last Name of the Defendant: ")
firstName = raw_input("Enter The First Name of the Defendant: ")

#Open Browser
browser = webdriver.Chrome()
browser.get('https://casesearch.epcounty.com/PublicAccess/default.aspx')
time.sleep(1)

#Press Criminal Case Records
searchButt = browser.find_elements_by_class_name('ssSearchHyperlink')
searchButt[0].click()
time.sleep(1)

#search
browser.find_element_by_xpath("//select[@name='SearchBy']/option[text()='Defendant']").click()
time.sleep(1)

#Last Name
lName = browser.find_element_by_name('LastName')
lName.send_keys(lastName)

#First Name
fName = browser.find_element_by_name('FirstName')
fName.send_keys(firstName)

#click search
browser.find_element_by_name('SearchSubmit').click()
time.sleep(1)

#Take screenshots for each case
elements = browser.find_elements_by_xpath("//a[contains(@href, 'CaseDetail.aspx?CaseID=')]")
i=0
while i < len(elements):
    elements[i].click()
    screenshotName = "screenshot" + str(i) + ".png"
    browser.save_screenshot(screenshotName)
    browser.back()
    elements = browser.find_elements_by_xpath("//a[contains(@href, 'CaseDetail.aspx?CaseID=')]")
    i = i+1



