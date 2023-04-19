import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestFacebook(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Edge()

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

    def test_upload_photo(self):
        self.loginfb()

        time.sleep(10)
        self.browser.find_element(By.XPATH, '//*[@id="facebook"]/body').click()
        time.sleep(5)
        self.browser.find_element(By.XPATH, '//*[@id="facebook"]/body').click()

        time.sleep(5)
        div_post = self.browser.find_element(By.XPATH,
                                             "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou']")
        time.sleep(2)
        div_post.click()
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//div[@aria-label='Ảnh/video']").click()
        time.sleep(2)
        input_image = self.browser.find_element(By.XPATH,
                                                "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/input")
        time.sleep(2)
        input_image.send_keys("D:\\tester\\Code\\test1.jpg")
        time.sleep(5)
        self.browser.find_element(By.XPATH, "//div[@aria-label='Đăng']").click()

    def test_post_text(self):
        self.loginfb()

        time.sleep(10)
        self.browser.find_element(By.XPATH, '//*[@id="facebook"]/body').click()
        self.browser.get("https://www.facebook.com/profile.php?id=100010138629252")
        time.sleep(5)
        self.browser.find_element(By.XPATH, '//*[@id="facebook"]/body').click()


if __name__ == '__main__':
    unittest.main()