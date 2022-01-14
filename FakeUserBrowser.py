#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 16:29:21 2022

@author: volodymyr
"""
#https://chromedriver.chromium.org/downloads


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from fake_useragent import UserAgent
import random

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

while True:
    user_input = input("Press Enter to create Chrome session..")
    options = Options()
    options.add_argument(f"window-size={random.randint(1000, 1800)},{random.randint(1000, 1800)}")

    ua = UserAgent()
    user_agent = ua.random

    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(executable_path=f'{os.getcwd()}//chromedriver', chrome_options=options)
    driver.get('https://whatismyipaddress.com/')
    clearConsole()
    print(f"The Chrome session was created successfully. Your user_agent: {user_agent}")





