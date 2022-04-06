import os
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, StringVar, messagebox
import pandas as pd
from container_img import create_excel_non_code_img


def select_file():
    """Select a file and save the path in filename variable"""
    path_filename = filedialog.askopenfilename()
    FILENAME.set(path_filename)


def select_directory():
    """Select a folder and save the path in directory variable"""
    path_directory = filedialog.askdirectory()
    DIRECTORY.set(path_directory)


def create_folder():
    """Сreates a folder where photos will be copied"""
    folder = FOLDERNAME.get()
    name_folder = folder
    path_directory = DIRECTORY.get()  # folder with all photo
    new_folder = r'{}\{}'.format(path_directory, name_folder)
    os.mkdir(new_folder)
    return new_folder


def create_list_txt():
    """Open file TXT and save data in list or dictionary"""
    path = FILENAME.get()
    file = open(path, 'r')
    list_with_vendor_code = []
    for article in file:
        list_with_vendor_code.append(article.strip())
    return list_with_vendor_code


def create_list_excel_test_with_read_null():
    """Open file EXCEL and save data in list or dictionary"""
    path = FILENAME.get()
    all_artickle = pd.read_excel(path)
    code_image_in_list = []
    for i in all_artickle['Артикул']:
        i = str(i)
        if len(i) < 6:
            code_image_in_list.append((6 - len(i)) * '0' + i)
        else:
            code_image_in_list.append(i)
    return code_image_in_list


def create_list_excel():
    """Open file EXCEL and save data in list or dictionary"""
    path = FILENAME.get()
    with pd.ExcelFile(path) as code_image:
        code_image_in_list = (pd.read_excel(code_image))['Артикул'].tolist()  # 'Sheet1'
    code_image_in_list = list(map(str, code_image_in_list))
    return code_image_in_list


def choice_checkbutton():
    """Return choice from checkbutton"""
    if choice.get() == 0:
        return '_0'
    elif choice.get() == 1:
        return '_1'
    elif choice.get() == 2:
        return ('_0', '_1')


def copy_pict_and_create_non_file_list(data_with_vendor_code, digit_in_the_end, folder):
    non_file_list = []
    for name_picture in data_with_vendor_code:
        f = f'{name_picture}{digit_in_the_end}.jpg'
        z = r'{}/{}'.format(path_directory, f)
        if os.path.exists(z):  # определяет содержится ли файл в заданной директории
            shutil.copy(z, folder)
        else:
            non_file_list.append(name_picture)
    return non_file_list


def function_copy_image():
    """Copies images that are in the excel file and in the folder with photos"""
    path_directory = DIRECTORY.get()
    non_file_list = []
    digit_in_the_end = choice_checkbutton()
    try:
        data_with_vendor_code = create_list_excel_test_with_read_null()  # create_list_excel()
    except FileNotFoundError:
        messagebox.showinfo(message='Проверьте правильность пути к файлу и его структуру')
        return
    if not path_directory:
        messagebox.showinfo(message='Проверьте правильность выбора папки с фотографиями')
        return
    try:
        folder = create_folder()
    except FileExistsError:
        messagebox.showinfo(
            message=f'Папка с именем {FOLDERNAME.get()} уже существует, удалите ее или не заполнено полу с вводом названия папки')
        return

    for name_picture in data_with_vendor_code:
        f = f'{name_picture}{digit_in_the_end}.jpg'
        z = r'{}/{}'.format(path_directory, f)
        if os.path.exists(z):  # определяет содержится ли файл в заданной директории
            shutil.copy(z, folder)
        else:
            non_file_list.append(name_picture)
            print(f'Файла под названием {name_picture} не существует в директории {z}')
    create_excel_non_code_img(non_file_list, folder)
    messagebox.showinfo(message='Program Finished')


# -----------------------------------------------------------
# Create main window and frame
window = Tk()
window.geometry('600x300-400+200')
window.title("Копирование фотографий")
mainframe = ttk.Frame(window)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe['padding'] = 20

FILENAME = StringVar()
DIRECTORY = StringVar()
FOLDERNAME = StringVar()

# -----------------------------------------------------------
# Create all widgets
path_file = ttk.Entry(mainframe, width=50, textvariable=FILENAME)
path_directory = ttk.Entry(mainframe, width=50, textvariable=DIRECTORY)
folder_name = ttk.Entry(mainframe, width=50, textvariable=FOLDERNAME)
name_label = Label(mainframe, text='Введите имя папки для фото')
button_select_file = ttk.Button(mainframe, text="Выберите Exel файл с кодами", width=30, command=select_file)
button_select_directory = ttk.Button(mainframe, text="Выберите папку с фотографиями", width=30,
                                     command=select_directory)

# -----------------------------------------------------------
# checkbutton_widjet
choice = BooleanVar()
choice.set(0)
check_box_box = ttk.Radiobutton(mainframe, text='Фото товара в упаковке', variable=choice, value=0)
check_box_piece = ttk.Radiobutton(mainframe, text='Фото штучного товара', variable=choice, value=1)
# check_box_all = ttk.Radiobutton(mainframe, text='Фото товара в упковке и штучного', variable=choice, value=2)

# ------------------------------------------------------------
# Button Launch
red_button = ttk.Button(mainframe, text='Запустить программу', width=30, command=function_copy_image)

# -----------------------------------------------------------
# Render on window
path_file.grid(column=1, row=0, pady=10)
path_directory.grid(column=1, row=1, pady=10)
folder_name.grid(column=1, row=2, pady=10)
name_label.grid(column=2, row=2, padx=10, pady=10)
button_select_file.grid(column=2, row=0, padx=10)
button_select_directory.grid(column=2, row=1, padx=10)
check_box_box.grid(column=2, row=3, pady=5, ipadx=16)
check_box_piece.grid(column=2, row=4, pady=5, ipadx=17)
# check_box_all.grid(column=2, row=5, pady=5)
red_button.grid(column=1, row=4, padx=10)

# -----------------------------------------------------------
# run program
window.mainloop()
