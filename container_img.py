import os
import xlsxwriter


def create_excel_non_code_img(non_img, directory_path):
    workbook = xlsxwriter.Workbook('{}/Нет картинок для следующих артикулов.xlsx'.format(directory_path))
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Артикул')
    #path_file_img = r'C:\Users\Maxim\Desktop\rename_pic'
    # x_all_files = [i.rstrip('.jpg .png .JPG') for i in os.listdir(path_file_img)]
    row = 1
    column = 0
    for item in non_img:
        worksheet.write(row, column, item)
        row += 1
    workbook.close()

