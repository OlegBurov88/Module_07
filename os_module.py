import os

print('Текущая директория', os.getcwd())

if os.path.exists('second'):  # принимает путь и возвращает True/False
    os.chdir('second')  # изменяем рабочую директорию
else:
    os.mkdir('second')  # создаём новую директорию
    os.chdir('second')  # изменяем рабочую директорию

print('Текущая директория', os.getcwd())
if not os.path.exists('third'):  # принимает путь и возвращает True/False
    os.makedirs(r'third/fourth')  # создаёт вложенные директории
print(os.listdir())  # список директорий внутри текущей(рабочей)

for i in os.walk('.'):  # вложенность директорий внутри текущей(рабочей)
    print(i)

os.chdir(r'E:\PycharmProjects\Module_07')
print('Текущая директория', os.getcwd())
print(os.listdir())

file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)
print(file)

os.startfile(file[9])
os.startfile('sample.txt')

print(os.stat(file[9]))
print(os.stat('sample.txt'))
print(os.stat(file[9]).st_size)
print(os.stat('sample.txt').st_file_attributes)
os.system('pip install random2')
