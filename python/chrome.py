# encoding=utf-8

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get("http://localhost:3000/login")

userInput = browser.find_element_by_css_selector('#username')
passInput = browser.find_element_by_css_selector('#password')
sleep(2)
userInput.send_keys('testbank')
passInput.send_keys('dh888888')
sleep(1)
loginBtn = browser.find_element_by_xpath('//*[@id="root"]/section[1]/main[1]/section[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/button[1]')
loginBtn.click()
sleep(2)

applyMenu = browser.find_element_by_css_selector('div#root > section > main > section > section > aside > div > ul > li:nth-of-type(3) > div')
applyMenu.click()
sleep(1)
applyItem = browser.find_element_by_css_selector('div#root > section > main > section > section > aside > div > ul > li:nth-of-type(3) > ul > li:nth-of-type(1)')
applyItem.click()
sleep(2)
applyBtn = browser.find_element_by_css_selector('div#root > section > main > section > section > main > div:nth-of-type(2) > div > div > div > div > div > div > table > tbody > tr > td:nth-of-type(4) > div > a')
applyBtn.click()

