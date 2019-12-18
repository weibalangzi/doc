# encoding=utf-8

from config import *
from selenium import webdriver
from time import sleep

    

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_ele_css(self, name):
        return self.browser.find_element_by_css_selector(name)

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get(TARGET_URL)

    def login_value_true(self):
        userEle = self.get_ele_css('#username')
        passEle = self.get_ele_css('#password')
        userEle.send_keys(self.username)
        passEle.send_keys(self.password)        
