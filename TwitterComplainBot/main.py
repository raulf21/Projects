from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

PROMISED_DOWN = 400
PROMISED_UP = 20
TWITTER_EMAIL = EMAIL
TWITTER_PASSWORD = PASSWORD

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        self.down = 0
        self.up = 0
    
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        while True:
            time.sleep(60)
            try:
                self.down =  self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
                self.up =  self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            except:
                time.sleep(2)
            else:
                break


        print(self.down,self.up)


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(10)
        email = self.driver.find_element(By.NAME,'text')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.NAME,'password')
        email.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        tweet_compose = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        twitter_button = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        twitter_button.click()

        time.sleep(2)

        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
