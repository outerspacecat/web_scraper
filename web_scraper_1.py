# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:24:01 2022

@author: Porsche
"""
from selenium import webdriver 

URL = 'https://www.amazon.co.uk/s?k=pet+strollers+for+cats&crid=CIKVMS8U73T6&sprefix=%2Caps%2C131&ref=nb_sb_ss_recent_1_0_recent'
x_path =  '/html/script[1]'
browser = webdriver.Chrome()
browser.get(URL)

browser.find_element_by_xpath(x_path).click()