from selenium import webdriver
import time

firstName = ''
lastName = ''
email = ''
passw = ''

url = 'https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Fcontacts.google.com%2F&followup=https%3A%2F%2Fcontacts.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

driver = webdriver.Chrome("/Users/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_id('identifierId').send_keys(email)
driver.find_element_by_id('identifierNext').click()

time.sleep(5)

driver.find_element_by_name('password').send_keys(passw)
driver.find_element_by_id('passwordNext').click()

time.sleep(10)

driver.find_element_by


