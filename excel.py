import xlsxwriter as xl
from book_info import *


class Excel:
    def __init__(self, book_data):
        self.book_data = book_data

    def create_excel(self, filename):
        workbook = xl.Workbook(filename)
        for book_key, book_details in self.book_data.items():
            for isbn, book_info in book_details.items():
                worksheet = workbook.add_worksheet(str(isbn))

                headers = ['ISBN', 'Title', 'Author', 'Genre', 'Edition', 'Date']
                header_format = workbook.add_format({
                    'font_name' : 'Bell MT',
                    'bold': True,
                    'font_color': 'black',
                    'bg_color': 'silver',
                    'border': 1
                })
                row = 3
                col = 3

                max_col = len(headers) - 1
                max_row = len(book_info) + 1 

                for i in range(max_col + 1):
                    worksheet.set_column(i, i, width=2.5*9)
                for i in range(max_row):
                    worksheet.set_row(i, height=2*9)

                for header in headers:
                    worksheet.write(row, col, header, header_format)
                    row += 1

                info_format = workbook.add_format({
                    'font_name': 'Bahnschrift SemiBold',
                    'font_color': 'black',
                    'bg_color': '#ADD8E6',
                    'border': 1
                })
                row = 3
                col = 4
                worksheet.write(row, col, isbn, info_format)
                row += 1
                for value in book_info.values():
                    worksheet.write(row, col, value, info_format)
                    row += 1

        workbook.close()
        print("Excel file created successfully.")

xlsx = Excel(book_data)
xlsx.create_excel(filename='Book_data.xlsx')