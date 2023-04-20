import unittest
import random
import time
from Test2.readexel.readbook1 import read_excel
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
        exel = read_excel(self)
        # Navigate to facebook.com
        self.browser.get(exel[0])
        self.browser.maximize_window()
        user_name = self.browser.find_element(By.ID, "email")
        # enter email
        user_name.send_keys(exel[1])
        pass_word = self.browser.find_element(By.ID, "pass")
        # enter password
        pass_word.send_keys(exel[2])

        btn_login = self.browser.find_element(By.NAME,"login")
        # click login
        btn_login.click()
        time.sleep(5)
        self.browser.find_element(By.XPATH,'//*[@id="facebook"]/body').click()

    def test_auto_cmt(self):
        exel = read_excel(self)
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

            b[i].send_keys( random.choice(exel[3:5]))
            b[i].send_keys(Keys.ENTER)
            time.sleep(10)
    def test_auto_cmt_img(self):
        #
        exel = read_excel(self)
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
            icon.send_keys(random.choice(exel[6:8]))
            time.sleep(10)
            inp.click()
            inp.send_keys(Keys.ENTER)
            time.sleep(5)

    def test_auto_cmt_text_img(self):
        # Lấy dữ liệu từ file excel
        exel = read_excel(self)
        # Đăng nhập
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
        btn_cmt = self.browser.find_elements(By.XPATH, '//*[@aria-label="Viết bình luận"]')
        icon_camera = self.browser.find_elements(By.XPATH, '//*[@type="file"]')
        input_cmt = self.browser.find_elements(By.XPATH, '//div[@class="xzsf02u x1a2a7pz x1n2onr6 x14wi4xw notranslate"]')
        for btn, icon, inp in zip(btn_cmt, icon_camera, input_cmt):
            btn.click()
            icon.send_keys(random.choice(exel[6:8]))
            time.sleep(10)
            inp.click()
            inp.send_keys(random.choice(exel[3:6]))
            inp.send_keys(Keys.ENTER)
            time.sleep(5)

