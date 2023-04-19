from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Khởi tạo trình duyệt
driver = webdriver.Chrome(ChromeDriverManager().install())

# Test case 1: Đăng nhập với tài khoản và mật khẩu chính xác
driver.get('https://www.facebook.com/')
username_input = driver.find_element(By.ID, 'email')
password_input = driver.find_element(By.ID, 'pass')
username_input.send_keys('hoagclone@gmail.com')
password_input.send_keys('hoang2002')

# Nhấn vào nút đăng nhập
login_button = driver.find_element(By.NAME, 'login')
login_button.click()

# Chờ cho trang web load xong và kiểm tra kết quả đăng nhập
try:
    success_msg = WebDriverWait(driver, 1).until(
        EC.title_contains('Facebook')
    )
    print('Đăng nhập thành công!')

except TimeoutException:
    try:
        error_msg = WebDriverWait(driver, 0).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Sai mật khẩu")]'))
        )
        print('Sai mật khẩu')
    except TimeoutException:
        print('Tài khoản không tồn tại')

# Khởi tạo trình duyệt
driver = webdriver.Chrome(ChromeDriverManager().install())

# Test case 2: Đăng nhập với mật khẩu không đúng
driver.get('https://www.facebook.com/')
username_input = driver.find_element(By.ID, 'email')
password_input = driver.find_element(By.ID, 'pass')
username_input.send_keys('hoagclone@gmail.com')
password_input.send_keys('abc12345')

# Nhấn vào nút đăng nhập
login_button = driver.find_element(By.NAME, 'login')
login_button.click()

# Chờ cho trang web load xong và kiểm tra kết quả đăng nhập
try:
    success_msg = WebDriverWait(driver, 1).until(
        EC.title_is('Facebook')
    )
    print('Đăng nhập thành công!')

except TimeoutException:
    try:
        error_msg = WebDriverWait(driver, 0).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Sai mật khẩu")]'))
        )
        print('Sai mật khẩu')
    except TimeoutException:
        print('Tài khoản không tồn tại')

# Khởi tạo trình duyệt
driver = webdriver.Chrome(ChromeDriverManager().install())

# Test case 3: Đăng nhập với tên đăng nhập không đúng
driver.get('https://www.facebook.com/')
username_input = driver.find_element(By.ID, 'email')
password_input = driver.find_element(By.ID, 'pass')
username_input.send_keys('abc12345@gmail.com')
password_input.send_keys('abc12345')

# Nhấn vào nút đăng nhập
login_button = driver.find_element(By.NAME, 'login')
login_button.click()

# Chờ cho trang web load xong và kiểm tra kết quả đăng nhập
try:
    success_msg = WebDriverWait(driver, 1).until(
        EC.title_is('Facebook')
    )
    print('Đăng nhập thành công!')

except TimeoutException:
    try:
        error_msg = WebDriverWait(driver, 0).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Sai mật khẩu")]'))
        )
        print('Sai mật khẩu')
    except TimeoutException:
        print('Tài khoản không tồn tại')
    
# Khởi tạo trình duyệt
driver = webdriver.Chrome(ChromeDriverManager().install())

# Test case 4: Đăng nhập với tài khoản và mật khẩu bỏ trống
driver.get('https://www.facebook.com/')
username_input = driver.find_element(By.ID, 'email')
password_input = driver.find_element(By.ID, 'pass')
username_input.send_keys('')
password_input.send_keys('')

# Nhấn vào nút đăng nhập
login_button = driver.find_element(By.NAME, 'login')
login_button.click()

# Chờ cho trang web load xong và kiểm tra kết quả đăng nhập
try:
    success_msg = WebDriverWait(driver, 1).until(
        EC.title_is('Facebook')
    )
    print('Đăng nhập thành công!')

except TimeoutException:
    try:
        error_msg = WebDriverWait(driver, 0).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Sai mật khẩu")]'))
        )
        print('Sai mật khẩu')
    except TimeoutException:
        print('Tài khoản không tồn tại')

# Khởi tạo trình duyệt
driver = webdriver.Chrome(ChromeDriverManager().install())

# Test case 5: Đăng nhập với tài khoản không tồn tại
driver.get('https://www.facebook.com/')
username_input = driver.find_element(By.ID, 'email')
password_input = driver.find_element(By.ID, 'pass')
username_input.send_keys('abc12234@gmail.com')
password_input.send_keys('123456789')

# Nhấn vào nút đăng nhập
login_button = driver.find_element(By.NAME, 'login')
login_button.click()

# chờ cho trang web load xong và kiểm tra kết quả đăng nhập
try:
    success_msg = WebDriverWait(driver, 1).until(
        EC.title_is('Facebook')
    )
    print('Đăng nhập thành công!')

except TimeoutException:
    try:
        error_msg = WebDriverWait(driver, 0).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Sai mật khẩu")]'))
        )
        print('Sai mật khẩu')
    except TimeoutException:
        print('Tài khoản không tồn tại')

# Đóng trình duyệt
driver.quit()
