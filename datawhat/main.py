import os
import pickle
import threading
import time

from pycli import cli
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from .scraper import despacito


class datawhat():
    def __init__(self, user_name_list, cli = False):
        """ pass cli object if cli functionality wanted """
        self.user_name_list = user_name_list
        self.first_run()
        self.cli = cli

    def first_run(self):
        # will need to pair whatsapp web with phone whatsapp
        self.driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
        self.driver.get("https://web.whatsapp.com/")
        answer = input('Is the phone connected successfully? (y/Y) -> ')
        if str(answer).strip().lower() == 'y':
            pickle.dump( self.driver.get_cookies() , open("cookies.pkl","wb"))
            return True

    def cycle(self, frequency):
        n = 0
        while True:
            self.send_message(despacito())
            print('{0} cycles made'.format(n))
            time.sleep(frequency)
            n += 1

    def open_chat(self, user_name):
        try:
            print ('Searching for user..... ' + user_name)
            web_obj = self.driver.find_element_by_xpath("//input[@title='Search or start new chat']")
            web_obj.send_keys(user_name)
            time.sleep(2)
            element = self.driver.find_element_by_xpath('//*[@title="{0}"]'.format(user_name))
            # ('//span[contains(text(),"{0}")]'.format(user_name))
            element.click()
            return True
        except:
            print ('O_o! \n No user found')
            element = self.driver.find_element_by_xpath('//button[@class="icon-search-morph"]')
            element.click()
            return False

    def send_message(self, message):
        for user_name in self.user_name_list:
            if self.open_chat(user_name):
                web_obj = self.driver.find_element_by_xpath("//div[@contenteditable='true']")
                if message is type("NoneType"):
                    message = "function completed - no value returned"
                web_obj.send_keys(message)
                web_obj.send_keys(Keys.RETURN)
            else: pass

    def command_input(self):
        if self.cli:
            self.send_message('type /help for list of functions, waiting for input: (checks every 4 seconds)')
            ans = False
            while not ans:
                """
                cycle through user list
                """
                time.sleep(4)
                
                usr_input = self.driver.find_elements_by_xpath(
                    "//span[contains(concat(' ', normalize-space(@class), ' '), 'selectable-text invisible-space copyable-text')]")
                usr_input = usr_input[-1].text
                if usr_input.startswith('/'):
                    ans = True
                    usr_input = usr_input[1:]

            print('user input: ' + str(usr_input))
            self.send_message(self.cli.cli_input(str(usr_input)))
        else:
            print('cli object not passed to datawhat')

"""
def not_first_run(self):
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
"""
