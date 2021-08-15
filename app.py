from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

class twitterBot:
    def __init__(self,usernam,password):
        self.usernam = usernam
        self.password = password
        self.bot=webdriver.Firefox()


    def login(self):
        bot=self.bot
        bot.get('https://instagram.com/')
        time.sleep(5)
        email=bot.find_element_by_name('username')
        password=bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.usernam)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(6)
    
    def likeTweet(self,Hashtag):
        bot=self.bot
        bot.get('https://www.instagram.com/explore/tags/'+Hashtag+' ')
        time.sleep(5)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(10)
            tweet=bot.find_elements_by_css_selector(".v1Nh3.kIKUG._bz0w [href]")
            links=[elem.get_attribute('href') for elem in tweet]
            print(links)
            for link in links:
                bot.get(link)
                try:
                    bot.find_element_by_css_selector(".fr66n").click()
                    time.sleep(6)
                except Exception as ex:
                    time.sleep(60)    




x='baderrdesigns'
y='1995Ziko.'
ed= twitterBot(x,y)
ed.login()
ed.likeTweet('Rajacasablanca')