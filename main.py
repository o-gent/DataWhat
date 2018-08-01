from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pickle

import time
import os
import threading

from scraper import despacito 

def main():
    # ask user and frequency 
    # ask if run before
    run = input('have you run this before? answer y/anything else ---> ')
    user_name = input('put exact username of person you want to Whatsacito ---> ')
    frequency = int(input('how often do you want to send despacito messages? (in seconds) --> '))
    if frequency < 10:
        print('some people just want to watch the world burn.. you must really hate the other person')
    
    if run == "y":
        not_first_run()
    else:
        driver = first_run()
    n = 0
    while True:
        find_user(driver, user_name)
        n += 1
        print('{0} cycles made'.format(n))
        time.sleep(frequency)

def first_run():
    # will need to pair whatsapp web with phone whatsapp, then login should be saved in cookies
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
    driver.get("https://web.whatsapp.com/")
    answer = input('Is the phone connected successfully? (y/Y) -> ')
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

    if str(answer).strip().lower() == 'y':
        return driver

def not_first_run():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
    driver.get("https://web.whatsapp.com/")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("http://www.google.com")
    driver.get("https://web.whatsapp.com/")
    return driver

def find_user(driver, user_name):
    user_name = user_name.strip()
    message = "despacito has " + str(despacito()) + " and counting!"

    user_name_list = user_name.split(',')

    for user_name in user_name_list:
        if user_name:
            send_message(driver, user_name.strip(), message)

def open_chat(driver, user_name):
    try:
        print ('Searching for user..... ' + user_name)
        web_obj = driver.find_element_by_xpath("//input[@title='Search or start new chat']")
        web_obj.send_keys(user_name)
        time.sleep(2)
        element = driver.find_element_by_xpath('//*[@title="{0}"]'.format(user_name))
        # ('//span[contains(text(),"{0}")]'.format(user_name))
        element.click()
        return True
    except:
        print ('O.o!\nNo user found..')
        element = driver.find_element_by_xpath('//button[@class="icon-search-morph"]')
        element.click()
        return False

def send_message(driver, user_name, message, is_interval=False):
    if open_chat(driver, user_name):
        web_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
        web_obj.send_keys(message)
        web_obj.send_keys(Keys.RETURN)

if __name__ == '__main__':
    main()
