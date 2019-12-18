from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(4)

    def follow(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag)
        time.sleep(4)

        posts = bot.find_elements_by_class_name('v1Nh3')
        count = 2
        inc = -1
        d = 1
        while d <= 2:
            for j in range(0, count):
                inc = inc + 1
                posts[inc].click()
                time.sleep(4)
                check = bot.find_element_by_class_name('oW_lN').text
                try:
                    if check == 'Follow':
                        bot.find_element_by_class_name('oW_lN').click()
                        d = d+1
                        if d == 3:
                            time.sleep(4)
                            bot.find_element_by_class_name('ckWGn').click()
                            break
                        time.sleep(4)
                except Exception as ex:
                    time.sleep(60)
                    print("Exception")
                bot.find_element_by_class_name('ckWGn').click()


usr = input("Enter user name")
pwd = input("Enter pasword")
hashtg = input("Enter a hashtag to follow")
test = InstaBot(usr, pwd)
test.login()
test.follow(hashtg)
