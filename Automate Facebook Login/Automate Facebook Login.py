from selenium import webdriver
from selenium.webdriver.commmon.keys import Keys
import time

# Take user id and password as input from the user
user_id = input('Enter user id of your facebook account: ')
password = input('Enter password')
print(user_id)
print(password)

# Path to firefox driver
cd = 'C:\\webdrivers\\firefoxdriver.exe'

browser = webdriver.Firefox(cd)
browser.get('https://www.facebook.com/')

# Detect user id and enter to box
user_box = browser.find_element_by_id('email')
user_box.send_keys(user_id)
# Detect password id and enter to the box
password_box = browser.find_element_by_id('pass')
password_box.send_keys(password)
# Detect login button amd click
login_box = browser.find_element_by_id("u_0_b")
login_box.click()