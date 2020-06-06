from openpyxl import *


if __name__ == '__main__':
    try:
        wb = load_workbook('users.xlsx')
        ws = wb.active
        ws['A4'] = 678
        wb.save('users.xlsx')
    except Exception as e:
        print(e)
