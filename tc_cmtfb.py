import unittest

import time

from prompt_toolkit.contrib.telnet.protocol import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class TestCmtFB(unittest.TestCase):
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
        # enter email
        user_name.send_keys("prothandao@gmail.com")
        pass_word = self.browser.find_element(By.ID, "pass")
        # enter password
        pass_word.send_keys("0898641520@a")

        btn_login = self.browser.find_element(By.NAME,"login")
        # click login
        btn_login.click()
        time.sleep(5)
        self.browser.find_element(By.XPATH,'//*[@id="facebook"]/body').click()

    def test_auto_cmt(self):
        self.loginfb()
        # Navigate to https://www.facebook.com/minh.dai.de
        self.browser.get("https://www.facebook.com/minh.dai.de")
        time.sleep(4)
        # Click screen
        self.browser.find_element(By.XPATH, '//*[@id="facebook"]/body').click()
        time.sleep(5)
        # pull down
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        # pull up
        self.browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(10)
        c = self.browser.find_element(By.XPATH, '//*[@aria-label="Viết bình luận"]')
        # click comment
        c.click()
        b = self.browser.find_elements(By.XPATH, '//div[@class="xzsf02u x1a2a7pz x1n2onr6 x14wi4xw notranslate"]')

        for i in range(0, len(b)):
            b[i].click()

            b[i].send_keys('a minh ơi a a a a a a a ')
            b[i].send_keys(Keys.ENTER)
            time.sleep(10)
    def test_auto_cmt_img(self):
        self.loginfb()
        self.browser.get("https://www.facebook.com/minh.dai.de")
        time.sleep(4)
        # Click screen
        self.browser.find_element(By.XPATH, '//*[@id="facebook"]/body').click()
        time.sleep(5)
        # pull down
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        # pull up
        self.browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(10)
        btn_cmt = self.browser.find_elements(By.XPATH, '//*[@aria-label="Viết bình luận"]')
        icon_camera = self.browser.find_elements(By.XPATH, '//*[@type="file"]')
        input_cmt = self.browser.find_elements(By.XPATH, '//div[@class="xzsf02u x1a2a7pz x1n2onr6 x14wi4xw notranslate"]')
        for btn, icon, inp in zip(btn_cmt, icon_camera, input_cmt):
            btn.click()
            icon.send_keys('D:\\tester\\Code\\test1.jpg')
            time.sleep(10)
            inp.click()
            inp.send_keys(Keys.ENTER)
            time.sleep(5)

    def test_auto_cmt_text_img(self):
        self.loginfb()
        self.browser.get("https://www.facebook.com/minh.dai.de")
        time.sleep(4)
        # Click screen
        self.browser.find_element(By.XPATH, '//*[@id="facebook"]/body').click()
        time.sleep(5)
        # pull down
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        # pull up
        self.browser.execute_script("window.scrollTo(0, 0);")
        time.sleep(10)
        btn_cmt = self.browser.find_elements(By.XPATH, '//*[@aria-label="Viết bình luận"]')
        icon_camera = self.browser.find_elements(By.XPATH, '//*[@type="file"]')
        input_cmt = self.browser.find_elements(By.XPATH, '//div[@class="xzsf02u x1a2a7pz x1n2onr6 x14wi4xw notranslate"]')
        for btn, icon, inp in zip(btn_cmt, icon_camera, input_cmt):
            btn.click()
            icon.send_keys('D:\\tester\\Code\\test1.jpg')
            time.sleep(10)
            inp.click()
            inp.send_keys('cmt test')
            inp.send_keys(Keys.ENTER)
            time.sleep(5)

