class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):  # определяем метод для сбора всех слов в *файле в словарь
        all_words = {}  # создаём словарь, в который будем собирать *файл: слова
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']  # список знаков для удаления
        for file_name in self.file_names:  # создаём цикл для итерации каждого файла
            list_line = []  # создаём список, куда будем собирать слова из каждого файла
            with open(file_name, encoding='utf-8') as file:
                for line in file:  # цикл для каждой строчки файла
                    line_l = line.lower()  # переводим строку в нижний регистр
                    for sign in punctuation:  # создаём цикл для удаления знаков
                        line_l = line_l.replace(sign, '')
                    list_line.extend(line_l.split())  # добавляем список слов из строки
                all_words[file_name] = list_line  # добавляем словарь 'название файла'(ключ) и 'списком слов'(значение)
        return all_words

    def find(self, word):  # определяем метод для поиска первого слова в файле
        all_words = self.get_all_words()
        word = word.lower()
        first_word_file = {}
        for i, j in all_words.items():
            if word in j:
                first_word_file[i] = j.index(word) + 1
        return first_word_file

    def count(self, word):  # определяем метод для поиска количества слов в файле
        all_words = self.get_all_words()
        word = word.lower()
        num_word_file = {}
        for i, j in all_words.items():
            if word in j:
                num_word_file[i] = j.count(word)
        return num_word_file


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

print()

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

print()

finder3 = WordsFinder('Rudyard Kipling - If.txt', )
print(finder3.get_all_words())
print(finder3.find('if'))
print(finder3.count('if'))

print()

finder4 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder4.get_all_words())
print(finder4.find('captain'))
print(finder4.count('captain'))

print()

finder0 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder0.get_all_words())
print(finder0.find('the'))
print(finder0.count('the'))
