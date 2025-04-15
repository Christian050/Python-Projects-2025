import pyautogui
import time
from time import sleep
import webbrowser
from selenium import webdriver
from webdriver_manager.firefox import FirefoxDriverManager
from getpass import getpass

Login_url = 'https://www.facebook.com/login.php'
num = str(input('Enter group ids, separated by commas: '))
list = num.split(',')
groupid = []
for i in list:
    groupid.append(i)
message = input('Enter your message')

class FacebookLogin():
    def __init__(self, email, password, browser='Firefox'):
        # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'Firefox':
            # Use Firefox
            self.driver = webdriver.Firefox(executable_path = FirefoxDriverManager().install())
            self.driver.get(Login_url)
            # Wait for sometime to load
            time.sleep(1)
    
    def login(self):
        # Provide email
        email_element = self.driver.find_element_by_id('email')
        email_element.send_keys(self.email)
        # Provide password
        password_element = self.driver.find_element_by_id('pass')
        password_element.send_keys(self.password)
        # Send mouse click
        login_button = self.driver.find_element_by_id('loginbutton')
        login_button.click()
        # Wait for 2 seconds for page to load
        time.sleep(2)
        
        for i in range(len(groupid)):
            link = 'https://www.facebook.com/groups'+groupid[i]
            self.driver(link)
            print('Waiting for a few seconds.....')
            time.sleep(45)
            self.driver.find_element_by_class_name('a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7').click()
            time.sleep(7)
            self.driver.switch_to.active_element.send_keys('message')
            time.sleep(7)
            self.driver.find_element_by_class_name('a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5').click()
            time.sleep(7)

if __name__ == '__main__':
    # Enter login credentials
    usr = input('Enter Email Id: ')
    pwd = getpass('Enter Password: ')
    fb_login = FacebookLogin(email=usr, password=pwd, browser='Firefox')
    fb_login.login()
    # time.sleep(5)