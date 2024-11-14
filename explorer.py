import tkinter
import os
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберете файл',
                                          filetypes=(('Текстовый файл', '.txt'),
                                                     ('Все файлы', '*')))
    text['text'] = '' + filename
    os.startfile(filename)


def info_window():
    info_window = tkinter.Tk()
    info_window.title('Инструкция')
    info_window.geometry('210x100')
    info_window.resizable(False, False)
    text_1 = tkinter.Label(info_window, text='Инструкция\n'
                                             'Нажмите на кнопку "Выбрать файл"\n'
                                             'для открытия текстового файла.\n'
                                             'После открытия файла на панели\n'
                                             '"Файл:" будет отображаться путь\n'
                                             'до открытого файла.')
    text_1.grid(column=0, row=0)


def about_window():
    about_window = tkinter.Tk()
    about_window.title('О программе')
    about_window.geometry('150x80')
    about_window.resizable(False, False)
    text_2 = tkinter.Label(about_window, text='О программе\n'
                                              'Проводник для открытия\n текстовых документов\n'
                                              'Версия 1.0\n'
                                              'Автор: Буров О.В.')
    text_2.grid(column=0, row=0)


window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x150')
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window, width=65, height=5, text='Файл:',
                     background='silver', foreground='blue')
text.grid(column=0, row=0, columnspan=3)
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл',
                               background='silver', foreground='blue',
                               command=file_select)
button_select.grid(column=0, row=1, pady=5)
info = tkinter.Button(window, height=3, width=10, text='Info',
                      background='silver', foreground='blue',
                      command=info_window)
info.grid(column=1, row=1)
about = tkinter.Button(window, height=3, width=10, text='About:',
                       background='silver', foreground='blue',
                       command=about_window)
about.grid(column=2, row=1)
window.mainloop()
