
import unittest
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LikeFB(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Edge()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def loginfb(self):
        # Navigate to facebook.com
        self.browser.get("https://www.facebook.com")
        self.browser.maximize_window()
        user_name = self.browser.find_element(By.ID, "email")
        user_name.send_keys("prothandao@gmail.com")
        pass_word = self.browser.find_element(By.ID, "pass")
        pass_word.send_keys("0898641520@a")
        btn_login = self.browser.find_element(By.NAME, "login")
        btn_login.click()
        time.sleep(5)
    def test_like(self):
        self.loginfb() # đăng nhập facebook
        time.sleep(5)
        # Click screen
        self.browser.find_element(By.
                                  XPATH, '//*[@id="facebook"]/body').click()
        time.sleep(5)
        # pull down
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        # pull up
        self.browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(10)
        # find element like
        a = self.browser.find_elements(By.XPATH,
                                    '//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi '
                                    'x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r '
                                    'x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg x1ja2u2z x1t137rt x1o1ewxj x3x9cwd'
                                    ' x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz x5ve5x3"]')
        for i in range(0, len(a)):
            time.sleep(2)
            # Click like
            a[i].click()
            print('like')
        time.sleep(10)
    def test_like_cx(self):
        self.loginfb()
        # # Navigate to hhttps://www.facebook.com/topcomments.vn
        # self.browser.get("https://www.facebook.com/beatvn.network")
        time.sleep(4)
        # Click screen
        self.browser.find_element(By.XPATH, '//*[@id="facebook"]/body').click()
        time.sleep(10)
        # pull down
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        # pull up
        self.browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(10)
        a = self.browser.find_elements(By.XPATH,
                                  '//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w'
                                  ' x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619'
                                  ' x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j'
                                  ' xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg x1ja2u2z'
                                  ' x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv'
                                  ' x1a2a7pz x5ve5x3"]')
        time.sleep(10)
        for i in range(len(a)):
            a[i].click()
            a[i].send_keys(Keys.TAB)
            pyautogui.press("enter")
            pyautogui.press("right")
            pyautogui.press("right")
            pyautogui.press("right")
            pyautogui.press("enter")
            pyautogui.press("enter")
            time.sleep(5)
