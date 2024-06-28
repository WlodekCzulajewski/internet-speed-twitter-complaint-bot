from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_DOWN = 750
PROMISED_UP = 40
URL_SPEEDTEST = "https://www.speedtest.net/"
TWITTER_EMAIL = "mypytestemail11@gmail.com"
TWITTER_PASSWORD = "cM5kb6LphmLd3@!S"
URL_TWITTER = "https://twitter.com/?lang=en"


class InternetSpeedTwitterBot():

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(URL_SPEEDTEST)
        self.driver.find_element(By.ID, value="onetrust-accept-btn-handler").click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, value="a.js-start-test").click()
        sleep(60)
        self.driver.execute_script("window.scrollTo(0, 400)")
        sleep(2)
        self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button').click()
        sleep(2)
        self.down = self.driver.find_element(By.CSS_SELECTOR, value="span.download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, value="span.upload-speed").text
        print(f"Down: {self.down}\nUp: {self.up}")

    def tweet_at_provider(self):
        self.driver.get(URL_TWITTER)
        sleep(5)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]/div').click()
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div').click()
        # Loging in

        sleep(7)
        email = self.driver.find_element(By.NAME, value="text")
        email.send_keys(TWITTER_EMAIL)
        sleep(2)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
        sleep(4)
        try:
            login = self.driver.find_element(By.NAME, value="text")
            login.send_keys("Net_spd_bot")
            sleep(3)
            self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
        except NoSuchElementException:
            pass
        sleep(3)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(TWITTER_PASSWORD)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
        # Tweeting

        sleep(5)
        tweet = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey internet provider, why is my speed {self.down}down/{self.up}up, "
                        f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]').click()
        try:
            self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div').click()
        except NoSuchElementException:
            pass
        print("Tweeted")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
