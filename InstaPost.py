import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import pyautogui

class InstaPost():
    def __init__(self, username=None, password=None, driverpath=None):
        self.browserProfile = webdriver.ChromeOptions()
        mobile_emulation = { 'deviceName':'Nexus 5'}
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browserProfile.add_experimental_option('mobileEmulation', mobile_emulation)
        self.browser = webdriver.Chrome(driverpath, options=self.browserProfile)
        self.username = username
        self.password = password
        print("create session: Profile: %s" %username)

    def signIn(self):
    	pyautogui.PAUSE = 1
    	pyautogui.FAILSAFE = True
    	self.browser.get('https://www.instagram.com/accounts/login/')
    	time.sleep(10)
    	usernameInput = self.browser.find_elements_by_css_selector('form input')[0]
    	passwordInput = self.browser.find_elements_by_css_selector('form input')[1]
    	usernameInput.send_keys(self.username)
    	passwordInput.send_keys(self.password)
    	time.sleep(2)
    	pyautogui.press('enter')
    	time.sleep(10)
    	self.browser.get('https://www.instagram.com/')
    	print("Logged In")
    	time.sleep(5)

    	# Cancel HomeButton
    	try:
    		cancelHomeScreen = self.browser.find_element_by_xpath("//button[text()='Cancel']")
    		cancelHomeScreen.click()
    	except NoSuchElementException:
    		pass
    		print("No Cancel Button here! Continue...")

    def newpost(self, uploading=None, hashtag=None):
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        time.sleep(5)
    	# click on Postbutton, add path in Upload Window and press enter
        try:
        	post = self.browser.find_element_by_xpath("//span[@aria-label='New Post']")
        	post.click()
        	print("Uploading")
        	
        	# Upload Window
        	time.sleep(5)
        	pyautogui.typewrite("/")
        	time.sleep(5)
        	pyautogui.press('backspace')
        	time.sleep(5)
        	pyautogui.typewrite(uploading, interval=1)
        	time.sleep(5)
        	pyautogui.press('enter')
        	time.sleep(5)
        	try:
        		expand = self.browser.find_element_by_xpath("//span[text()='Expand']")
        		expand.click()
        	except NoSuchElementException:
        		pass
        	#press Next
        	time.sleep(5)
        	nextbutton = self.browser.find_element_by_xpath('//button[text()="Next"]')
        	nextbutton.click()
        	time.sleep(5)
        	#add Hashtag and press share
        	wrthash = self.browser.find_element_by_xpath("//textarea").send_keys(hashtag)
        	time.sleep(5)
        	share = self.browser.find_element_by_xpath("//button[text()='Share']")
        	share.click()
        	time.sleep(5)
        	print("Posted!")
        except NoSuchElementException:
            pass
            print("Can't find Upload Button :(")
            
    def closeBrowser(self):
        self.browser.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()
