import io
from pprint import pprint

name = 'sample2.txt'
file = open(name, 'r', encoding='utf-8')  # r - read(чтение), w - write(запись), a - append(добавление)
print(file.tell())
pprint(file.read())
print(file.tell())
print(file.writable())  # можно ли зависать в файл
print(file.readable())  # можно ли прочитать в файл
print(file.seekable())  # можно ли перемещать курсор в файле
file.seek(14)
print(file.tell())
file.seek(55)
print(file.tell())
file.close()

file = open(name, 'a')
file.seek(55)
file.write('New text\n')
print(file.tell())
file.close()

# print(file)
# pprint(file.read())
# file.close()
# name_2 = 'sample2.txt'
# file = open(name_2, 'w')
# file.write('Hello world!')
# file.close()
# name_2 = 'sample2.txt'
# file = open(name_2, 'a')
# file.write('\nhello')
# file.close()
#
# file = open(name, 'r')
# print(file.tell())
# pprint(file.read())
# print(file.tell())
# pprint(file.read())
# print(file.seek(93))
# print(file.tell())
# pprint(file.read())
file.close()
