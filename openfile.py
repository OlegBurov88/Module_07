from pprint import pprint

name = 'sample.txt'
file = open(name, 'r')  # r - read(чтение), w - write(запись), a - append(добавление)
print(file)
pprint(file.read())
file.close()
name_2 = 'sample2.txt'
file = open(name_2, 'w')
file.write('Hello world!')
file.close()
name_2 = 'sample2.txt'
file = open(name_2, 'a')
file.write('\nhello')
file.close()

file = open(name, 'r')
print(file.tell())
pprint(file.read())
print(file.tell())
pprint(file.read())
print(file.seek(93))
print(file.tell())
pprint(file.read())
file.close()
