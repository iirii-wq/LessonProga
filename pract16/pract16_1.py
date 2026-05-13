print('Шумоподавлениe')

in_str = input('введите строку слов >>> ')
word_list = in_str.split()

uniq_word = set(word_list)
print("Количество >>> ", len(uniq_word))

sort_word = sorted(uniq_word)
print("Слова >>> ", sort_word)