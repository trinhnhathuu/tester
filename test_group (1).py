import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def launchBrowser():
    browser = webdriver.Edge()
    browser.get("https://www.facebook.com")
    return browser

browser = launchBrowser()
browser.maximize_window()

#Đăng Nhập
def Login():
    username = browser.find_element(By.ID, "email").send_keys("gamesmail0308@gmail.com")
    password = browser.find_element(By.ID, "pass").send_keys("Huy456")
    login = browser.find_element(By.NAME, "login").click()
    actions = ActionChains(browser)
    actions.key_down(Keys.ENTER)
    actions.perform()
    
#Di chuyển đến Group
def NavigateToGroup():
    browser.get("https://www.facebook.com/groups/")
    ActionChains(browser).move_by_offset(10 , 10).click().perform()
    time.sleep(3)

#Xem thêm các nhóm
def Discover():
    NavigateToGroup()
    browser.find_element(By.XPATH, "//span[contains(text(),'Khám phá')]").click()
    time.sleep(3)

#Tạo nhóm mới
def CreateGroup():
    NavigateToGroup()
    create = browser.find_element(By.PARTIAL_LINK_TEXT, 'Tạo nhóm mới')
    create.click()
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "label[aria-label='Tên nhóm']").send_keys("Test Group1")
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "label[aria-label='Chọn quyền riêng tư']").click()
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "div[class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xe8uvvx x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xjyslct x9f619 x1ypdohk x78zum5 x1q0g3np x2lah0s xnqzcj9 x1gh759c xdj266r xat24cr x1344otq x1de53dj x1n2onr6 x16tdsg8 x1ja2u2z x1y1aw1k xwib8y2']").click()
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "div[aria-label='Tạo']").click()
    time.sleep(3)

#Tìm kiếm nhóm
def Search():
    NavigateToGroup()
    search_group = browser.find_element(By.XPATH, "//input[@aria-label='Tìm kiếm nhóm']")
    time.sleep(3)
    search_group.click()
    time.sleep(3)
    search_group.send_keys("python")
    search_group.send_keys(Keys.ENTER)
    time.sleep(3)

#Tìm kiếm nhóm mới và tham gia
def FindnJoin():
    NavigateToGroup()
    browser.find_element(By.XPATH, "//input[@aria-label='Tìm kiếm nhóm']").click()
    time.sleep(3)
    browser.get("https://www.facebook.com/groups/690658562491320/")
    time.sleep(3)
    browser.find_element(By.XPATH, "//span[contains(text(),'Tham gia nhóm')]").click()
    time.sleep(3)

#Đăng text trong nhóm đã tham gia
def PostText():
    NavigateToGroup()
    browser.find_element(By.XPATH, "//span[contains(text(),'Test Group')]").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//span[contains(text(),'Bạn viết gì đi')]").click()
    time.sleep(3)
    actions = ActionChains(browser)
    actions.send_keys('This is my 1st post in this group!!!')
    actions.perform()
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "div[aria-label='Đăng']").click()
    time.sleep(3)

#Đăng ảnh/video trong nhóm đã tham gia
def PostImage():
    NavigateToGroup()
    browser.find_element(By.XPATH, "//span[contains(text(),'Test Group')]").click()
    time.sleep(10)
    browser.find_element(By.XPATH, "//span[contains(text(), 'Ảnh/video')]").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//input[@type='file']").send_keys("C:/Users/ACER/Downloads/tft.png")
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "div[aria-label='Đăng']").click()
    time.sleep(3)

#Tìm kiếm trong nhóm đã tham gia
def FindInGroup():
    NavigateToGroup()
    browser.find_element(By.XPATH, "//span[contains(text(),'Python Programming')]").click()
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "div[aria-label='Tìm kiếm']").click()
    time.sleep(3)
    find = browser.find_element(By.XPATH, "//input[@aria-label='Tìm kiếm trong nhóm này']")
    time.sleep(3)
    find.send_keys("sorting algorithms")
    find.send_keys(Keys.ENTER)
    time.sleep(3)

#Rời khỏi nhóm đã tham gia
def Out():
    NavigateToGroup()
    browser.find_element(By.XPATH, "//span[contains(text(),'Python Programming')]").click()
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "div[aria-label='Xem thêm']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, "//span[contains(text(),'Rời nhóm')]").click()
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "div[aria-label='Rời khỏi nhóm']").click()
    time.sleep(3)

Login()
time.sleep(3)

NavigateToGroup()
time.sleep(3)

Discover()
time.sleep(3)

CreateGroup()
time.sleep(3)

Search()
time.sleep(3)

FindnJoin()
time.sleep(3)

PostText()
time.sleep(3)

PostImage()
time.sleep(3)

FindInGroup()
time.sleep(3)

Out()
time.sleep(3)

browser.quit()