import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


class TestUploadPhoto(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_upload_photo(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.facebook.com")
        # Login
        email = driver.find_element(By.XPATH,"//input[@name='email']")
        email.send_keys("prothandao@gmail.com")
        password = driver.find_element(By.XPATH,"//input[@name='pass']")
        password.send_keys("0898641520@a")
        password.send_keys(Keys.ENTER)

        # chờ 5 giây để trang web load xong
        driver.get("https://www.facebook.com/")
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="facebook"]/body').click()
        # click vào nút đăng ảnh
        driver.find_element(By.XPATH, "//*[contains(text(), 'Ảnh/video')]").click() 
        time.sleep(5)
        # chọn ảnh để upload
        upload_photo_button = driver.find_element(By.XPATH,"//input[@type='file']")
        upload_photo_button.send_keys("D:\\tester\\Code\\test1.jpg")
        # chờ 5 giây để ảnh upload lên
        time.sleep(5)
        # nhập mô tả cho ảnh
        photo_description = driver.find_element(By.XPATH,"//div[@role='textbox']")
        photo_description.send_keys("Mô tả image")
        # click nút đăng ảnh
        time.sleep(5)
        
        driver.find_element(By.XPATH,"//span[contains(text(),'Đăng')]").click()
        # chờ 5 giây để ảnh được đăng lên thành công
        time.sleep(5)

      # # kiểm tra bài đăng hiển thị trên trang cá nhân
      #   try:
      #       # Tìm kiếm phần tử liên quan đến bài đăng, chẳng hạn như một thẻ div có chứa nội dung của bài đăng
      #       post_element = driver.find_element(By.XPATH, "//div[contains(text(), '{}')]".format(upload_photo_button))
      #       # Kiểm tra xem phần tử đó có hiển thị trên trang hay không
      #       assert post_element.is_displayed()
      #   except:
      #       # Nếu không tìm thấy phần tử hoặc không hiển thị, báo lỗi
      #       self.fail("Bài đăng không hiển thị trên trang cá nhân của người dùng")

    def tearDown(self):
        self.driver.quit()


