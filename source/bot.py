from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import os
import time
import datetime


class Bot:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        s=Service('C:/Users/samee/OneDrive/Desktop/INSTA/source/chromedriver.exe')
        self.driver = webdriver.Chrome(service = s)  # service = s

        self.driver.maximize_window()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')

        time.sleep(100)
        self.login()


# self=object()
# self = type('', (), {})()
# __init__(self, "sameeksha003", "Sam.Sh2401")
ig = Bot("sameeksha003", "Sam.Sh2401")
# ig.login()
