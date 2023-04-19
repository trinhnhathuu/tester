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
    

#function login
def login():
    user_name = browser.find_element(By.ID, "email").send_keys("0366162848")
    pass_word = browser.find_element(By.ID, "pass").send_keys("Tungpro312")
    btn_login = browser.find_element(By.NAME,"login").click()
    actions = ActionChains(browser)
    actions.key_down(Keys.ENTER)
    actions.perform()
    browser.get("https://www.facebook.com/")

#1. Tìm kiếm theo từ khóa: Kiểm tra xem ô tìm kiếm có hoạt động chính xác khi nhập từ khóa vào.
#Ví dụ: nhập tên người dùng, trang, nội dung bài đăng, hoặc chủ đề để kiểm tra kết quả trả về có chính xác không.

#function search by keyword
def searchByKeyword():
    actions = ActionChains(browser)
    actions.send_keys(Keys.RETURN)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("tung")
    search.send_keys(Keys.ENTER)
    assert "tung" in browser.page_source
    
#2.Tìm kiếm bằng ngôn ngữ tự nhiên: Kiểm tra khả năng của ô tìm kiếm để hiểu và tìm kiếm các câu hỏi hoặc
# yêu cầu bằng ngôn ngữ tự nhiên. Ví dụ: "Tìm kiếm những ảnh của bạn bè tại New York",
# hoặc "Tìm kiếm những bài đăng được chia sẻ trong tuần qua".

#function search in natural language
def SearchInNaturalLanguage():
    browser.get("https://www.facebook.com")
    actions = ActionChains(browser)
    actions.send_keys(Keys.RETURN)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("những chuyện hot nhất tuần qua")
    search.send_keys(Keys.ENTER)
    assert "những chuyện hot nhất tuần qua" in browser.page_source

#3. Tìm kiếm theo mục đích: Kiểm tra xem ô tìm kiếm có cung cấp các lựa chọn tìm kiếm theo mục đích,
# chẳng hạn như tìm kiếm người dùng, trang, nhóm, bài đăng, ảnh, video, v.v. Ví dụ: Kiểm tra khả năng
# tìm kiếm các nhóm liên quan đến chủ đề "Du lịch" hoặc tìm kiếm các trang Facebook có liên quan đến "Âm nhạc".

#function search by purpose
def SearchByPurpose():
    browser.get("https://www.facebook.com")
    actions = ActionChains(browser)
    actions.send_keys(Keys.RETURN)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("những chuyện hot nhất tuần qua")
    search.send_keys(Keys.ENTER)
    assert "những chuyện hot nhất tuần qua" in browser.page_source
    time.sleep(2)
    browser.get("https://www.facebook.com/search/posts?q=nh%E1%BB%AFng%20chuy%E1%BB%87n%20hot%20nh%E1%BA%A5t%20tu%E1%BA%A7n%20qua")
    time.sleep(2)
    assert "những chuyện hot nhất tuần qua" in browser.page_source
    browser.get("https://www.facebook.com/search/people?q=nh%E1%BB%AFng%20chuy%E1%BB%87n%20hot%20nh%E1%BA%A5t%20tu%E1%BA%A7n%20qua")
    time.sleep(2)
    assert "những chuyện hot nhất tuần qua" in browser.page_source
    browser.get("https://www.facebook.com/search/photos?q=nh%E1%BB%AFng%20chuy%E1%BB%87n%20hot%20nh%E1%BA%A5t%20tu%E1%BA%A7n%20qua")
    time.sleep(2)
    assert "những chuyện hot nhất tuần qua" in browser.page_source
    browser.get("https://www.facebook.com/search/videos?q=nh%E1%BB%AFng%20chuy%E1%BB%87n%20hot%20nh%E1%BA%A5t%20tu%E1%BA%A7n%20qua")
    time.sleep(2)
    assert "những chuyện hot nhất tuần qua" in browser.page_source
    browser.get("https://www.facebook.com/search/pages?q=nh%E1%BB%AFng%20chuy%E1%BB%87n%20hot%20nh%E1%BA%A5t%20tu%E1%BA%A7n%20qua")
    time.sleep(2)
    assert "những chuyện hot nhất tuần qua" in browser.page_source
    browser.get("https://www.facebook.com/search/places?q=nh%E1%BB%AFng%20chuy%E1%BB%87n%20hot%20nh%E1%BA%A5t%20tu%E1%BA%A7n%20qua")
    time.sleep(2)
    assert "những chuyện hot nhất tuần qua" in browser.page_source
    browser.get("https://www.facebook.com/search/groups?q=nh%E1%BB%AFng%20chuy%E1%BB%87n%20hot%20nh%E1%BA%A5t%20tu%E1%BA%A7n%20qua")
    time.sleep(2)
    browser.get("https://www.facebook.com/search/events?q=nh%E1%BB%AFng%20chuy%E1%BB%87n%20hot%20nh%E1%BA%A5t%20tu%E1%BA%A7n%20qua")
    time.sleep(2)
    assert "những chuyện hot nhất tuần qua" in browser.page_source

#4. Tìm kiếm bộ lọc: Kiểm tra khả năng của ô tìm kiếm để áp dụng các bộ lọc để chính xác hóa kết quả tìm kiếm.
# Ví dụ: kiểm tra khả năng để sắp xếp kết quả tìm kiếm theo thứ tự thời gian, độ phổ biến hoặc độ tương đồng.

# function Search for filter
def SearchForFilter():
    browser.get("https://www.facebook.com")
    actions = ActionChains(browser)
    actions.send_keys(Keys.RETURN)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("thú cưng đáng yêu")
    search.send_keys(Keys.ENTER)
    assert "thú cưng đáng yêu" in browser.page_source
    time.sleep(3)
    browser.get("https://www.facebook.com/search/posts?q=thú%20cưng%20đáng%20yêu")
    time.sleep(2)
    recently = browser.find_elements(By.XPATH,"//div[@class='x1ja2u2z x1a2a7pz x14nfmen x9f619 x1rg5ohu x1hc1fzr x6ikm8r x10wlt62 xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1eub6wo x19991ni x1d72o xyi19xy x1ccrb07 xtf3nb5 x1pc53ja xxk0z11 x187nhsf xdj266r x11i5rnm x4vbgl9 x1mh8g0r']")
    for i in recently:
        i.click()
        time.sleep(3)
    time.sleep(2)
    createAt = browser.find_element(By.XPATH,"//div[@class='x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x1ypdohk xdl72j9 x2lah0s xe8uvvx x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz xhk9q7s x1otrzb0 x1i1ezom x1o6z2jb x9f619 x78zum5 xl56j7k x1xmf6yo x1y1aw1k x1sxyh0 xwib8y2 xurb0ha xh8yej3']")
    createAt.click()
    time.sleep(2)
    chooseYear = browser.find_elements(By.XPATH,"//div[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xe8uvvx x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xjyslct x9f619 x1ypdohk x78zum5 x1q0g3np x2lah0s xnqzcj9 x1gh759c xdj266r xat24cr x1344otq x1de53dj xz9dl7a xsag5q8 x1n2onr6 x16tdsg8 x1ja2u2z']")
    chooseYear[1].click()
    time.sleep(2)
    fromPost = browser.find_element(By.XPATH,"//div[@class='x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x78zum5 x1a2a7pz']")
    fromPost.click()
    chooseFromPost = browser.find_elements(By.XPATH,"//div[@class='x6s0dn4 x1ypdohk x78zum5 x6ikm8r x10wlt62 x1n2onr6 xi2jdih x1lq5wgf xgqcy7u x30kzoy x9jhf4c xdj266r xat24cr x1y1aw1k x1sxyh0 xwib8y2 xurb0ha']")
    chooseFromPost[4].click()
    time.sleep(2)
    locationTag = browser.find_elements(By.XPATH,"//div[@class='x9f619 x78zum5 xdt5ytf xh8yej3']")
    locationTag[1].click()
    time.sleep(2)
    inputLocation = browser.find_element(By.XPATH,"//input[@class='x1qlo5rv x5zoitm x1953sy1 xnjxffw x1lq5wgf xgqcy7u x30kzoy x9jhf4c x9f619 xzsf02u x6prxxf x5yr21d x1a2a7pz x1a8lsjc xqmdsaz xurb0ha x96k8nx xh8yej3 x443n21 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    inputLocation.send_keys("Hà Nội")
    time.sleep(2)
    locationDetais = browser.find_elements(By.XPATH,"//div[@class='x6s0dn4 x1ypdohk x78zum5 x6ikm8r x10wlt62 x1n2onr6 xi2jdih x1lq5wgf xgqcy7u x30kzoy x9jhf4c xdj266r xat24cr x1y1aw1k x1sxyh0 xwib8y2 xurb0ha']")
    locationDetais[0].click()


    
#5. Tìm kiếm địa điểm: Kiểm tra khả năng của ô tìm kiếm để tìm kiếm địa điểm 
# hoặc địa điểm liên quan đến các hoạt động cụ thể, chẳng hạn như tìm kiếm các nhà hàng, khách sạn hoặc địa điểm tham quan.
    
# function Search for a place
def SearchForPlace():
    browser.get("https://www.facebook.com")
    actions = ActionChains(browser)
    actions.send_keys(Keys.RETURN)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("nhà hàng gần tôi")
    search.send_keys(Keys.ENTER)
    assert "No results found." not in browser.page_source
    time.sleep(2)
    browser.get("https://www.facebook.com/search/places?q=nhà%20hàng%20gần%20tôi")
    puporses = browser.find_elements(By.XPATH,"//div[@class='x1ja2u2z x1a2a7pz x14nfmen x9f619 x1rg5ohu x1hc1fzr x6ikm8r x10wlt62 xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1eub6wo x19991ni x1d72o xyi19xy x1ccrb07 xtf3nb5 x1pc53ja xxk0z11 x187nhsf xdj266r x11i5rnm x4vbgl9 x1mh8g0r']") 
    for puporse in puporses:
        puporse.click()
        time.sleep(2)
    locations =  browser.find_element(By.XPATH,"//div[@class='x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x78zum5 x1a2a7pz']")
    locations.click()
    time.sleep(2)
    inputLocation = browser.find_element(By.XPATH,"//input[@class='x1qlo5rv x5zoitm x1953sy1 xnjxffw x1lq5wgf xgqcy7u x30kzoy x9jhf4c x9f619 xzsf02u x6prxxf x5yr21d x1a2a7pz x1a8lsjc xqmdsaz xurb0ha x96k8nx xh8yej3 x443n21 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    inputLocation.send_keys("Đà Nẵng")
    time.sleep(2)
    locationDetais = browser.find_elements(By.XPATH,"//div[@class='x6s0dn4 x1ypdohk x78zum5 x6ikm8r x10wlt62 x1n2onr6 xi2jdih x1lq5wgf xgqcy7u x30kzoy x9jhf4c xdj266r xat24cr x1y1aw1k x1sxyh0 xwib8y2 xurb0ha']")
    locationDetais[0].click()
    assert "No results found." not in browser.page_source


#6. Tìm kiếm trong ngôn ngữ khác: Kiểm tra khả năng của ô tìm kiếm để tìm kiếm các nội dung trong ngôn ngữ khác nhau. 
# Ví dụ: kiểm tra khả năng của ô tìm kiếm để tìm kiếm các trang, bài đăng hoặc ảnh trong các ngôn ngữ khác nhau.

#function Search in another language
def SearchInAnotherLanguage():
    browser.get("https://www.facebook.com")
    actions = ActionChains(browser)
    actions.send_keys(Keys.RETURN)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("good food")
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.get("https://www.facebook.com")
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("طعام جيد")
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.get("https://www.facebook.com")
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("いい食べ物")
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.get("https://www.facebook.com")
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("美食")
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.get("https://www.facebook.com")
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("좋은 음식")
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.get("https://www.facebook.com")
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("сайн хоол")
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.get("https://www.facebook.com")
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("อาหารที่ดี")
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.get("https://www.facebook.com")
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("boa comida")
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.get("https://www.facebook.com")
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("хорошая еда")
    search.send_keys(Keys.ENTER)
    assert "Facebook" in browser.title
    


#7.Tìm kiếm với từ khóa không chính xác: Kiểm tra khả năng của ô tìm kiếm để tìm kiếm các nội dung với các từ khóa
# không chính xác hoặc đánh sai chính tả. Ví dụ: kiểm tra khả năng của ô tìm kiếm để tìm kiếm các kết quả với các 
# từ khóa không chính xác hoặc đánh sai chính tả.

#function Search with incorrect keywords
def SearchWithIncorrectKeywords():
    browser.get("https://www.facebook.com")
    actions = ActionChains(browser)
    actions.send_keys(Keys.RETURN)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("     ")
    search.send_keys(Keys.ENTER)
    time.sleep(3)
    browser.get("https://www.facebook.com")
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("sndfjbasjhfnuaewyfuaegwyfgaewyfgweyfcgbwyfbsdbgvdshsbghj")
    search.send_keys(Keys.ENTER)
    time.sleep(3)
    browser.get("https://www.facebook.com")
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("@#!$%^**()*15151151^%$#@$@#")
    search.send_keys(Keys.ENTER)
    time.sleep(3)
    browser.get("https://www.facebook.com")
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("tồi náy ân gí đẫy")
    search.send_keys(Keys.ENTER)
    time.sleep(3)
    browser.get("https://www.facebook.com")
    search = browser.find_element(By.XPATH,"//input[@class='x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj x1sxyh0 xdvlbce xurb0ha x1vqgdyp x1xtgk1k x17hph69 xo6swyp x1ad04t7 x1glnyev x1ix68h3 x19gujb8']")
    search.send_keys("jfhjsdhgdadga1234567890")
    search.send_keys(Keys.ENTER)
    assert browser.current_url != "https://www.facebook.com/search/top/?q=jfhjsdhgdadga1234567890", "Search function doesn't work properly"



#8 function Kiểm tra xem nút "Home" có hoạt động đúng khi được nhấn.
def home():
    browser.get("https://www.facebook.com")
    actions = ActionChains(browser)
    actions.send_keys(Keys.RETURN)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    home_button = browser.find_element(By.XPATH,"//div[@class='x6s0dn4 x9f619 x78zum5 x1iyjqo2 x1s65kcs x1d52u69 xixxii4 x17qophe x13vifvy xzkaem6']")
    time.sleep(3)   
    home_button.click()
    assert browser.current_url == "https://www.facebook.com/", "Home button doesn't work properly"

#9 Kiểm tra xem nút "Menu" có hiển thị và hoạt động đúng khi được nhấn.
def menu():
    actions = ActionChains(browser)
    actions.send_keys(Keys.RETURN)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    time.sleep(1)
    menu_button = browser.find_element(By.XPATH,"//div[@class='x78zum5 x1n2onr6']")
    time.sleep(3)
    menu_button.click()
    time.sleep(2)
    menu_items = browser.find_elements(By.XPATH,"//div[@role='listitem']")
    time.sleep(2)
    assert len(menu_items) > 0, "Menu button doesn't work properly"
    time.sleep(2)
    accout = browser.find_element(By.XPATH,"//a[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x1a2a7pz x6s0dn4 x1lliihq xl56j7k x1xmf6yo xw3qccf x1e56ztr xsgj6o6 x14atkfc']")
    accout.click()
    time.sleep(2)
    assert browser.current_url != "https://www.facebook.com/", "Menu button doesn't work properly"
 

    

login()
time.sleep(2)
menu()
time.sleep(2)
home()
time.sleep(2)
searchByKeyword()
time.sleep(2)
SearchInNaturalLanguage()
time.sleep(2)
SearchByPurpose()
time.sleep(2)
SearchForFilter()
time.sleep(2)
SearchForPlace()
time.sleep(2)
SearchInAnotherLanguage()
time.sleep(2)
SearchWithIncorrectKeywords()
time.sleep(5)
browser.quit()
