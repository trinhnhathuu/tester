import openpyxl
def read_excel(self):
    wb = openpyxl.load_workbook('../excel/Book1.xlsx')
    # lấy sheet login
    login = wb['Login']

    # ví dụ: đọc giá trị của ô B1
    b1_login = login[f'B1'].value
    b2_login = login[f'B2'].value
    b3_login = login[f'B3'].value

    comment = wb['Comment']
    b1_cmt = comment[f'B1'].value
    b2_cmt = comment[f'B2'].value
    b3_cmt = comment[f'B3'].value
    b5_cmt = comment[f'B5'].value
    b6_cmt = comment[f'B6'].value

    return b1_login, b2_login, b3_login,b1_cmt,b2_cmt,b3_cmt,b5_cmt,b6_cmt



