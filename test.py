# Глянем ка что там вообще за символы
temp = set()
for i in text:
    temp.add(i)
temp.remove(' ') 
temp.remove('\n')
ltemp = list(temp)
ltemp.sort()
ltemp = ['['] + ltemp + [']'] # А вдруг что-то непечатное, типа табуляции, в начале или в конце строки
print(*ltemp, sep = '')

# Говорят что вся пунктуация здесь:
import string
punctuation = string.punctuation
print(punctuation)
add = '—«»0123456789'
punct = set(punctuation)
for i in add:
    punct.add(i)
punct.add(i)
punct.remove('-')
ltemp = list(punct)
ltemp.sort()
print(*ltemp, sep='')

punctuation = '!"#$%&\'()*+,./0123456789:;<=>?@[\]^_`{|}~«»—'
print(punctuation)
print()

# Пробелы вмеесто пунктуации
for i in punctuation:
    text = text.replace(i, ' ')

# И запишем в файл
with open('punct.txt', mode = 'wt', encoding = 'utf-8') as f:
    f.write(text)

# слова в список
words = text.split()

with open('words.txt', mode = 'wt', encoding = 'utf-8') as f:
    for i in words:
        f.write(i)
        f.write(';')

# все к нижнему регистру
temp = list(map(lambda x: x.lower(), words))
list_text = [i.lower() for i in words]
print(list_text)


############################################################################
# Здесь хотелось бы задать вопрос: "Что лучше использовать в данном случае?"
# И заодно проверить, читает ли кто-нибудь мой код ;)
#####################################################

# И запишем в файл через ";"
with open('t3.txt', mode = 'wt', encoding = 'utf-8') as f:
    for i in list_text:
        f.write(i)
        f.write(';')

#######################
# Проведем лемматизацию
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

# Не будем мудрить с лингвистикой.
# Будем считать что первая же форма правильная
normal_form_word = [morph.parse(i)[0].normal_form for i in list_text] # Опять же, можно было map()
del morph # Модуль больше не нужен. Автор модуля советует экономить память)

print(normal_form_word)
print()

# И запишем в файл "то что было" -> "то что стало"
with open('t3pro.txt', mode = 'wt', encoding = 'utf-8') as f:
    for i in range(len(list_text)):
        f.write(list_text[i])
        f.write(' -> ')
        f.write(normal_form_word[i])
        f.write('\n')

# Визуально нашел только 2 ошбки: "аркадьич -> аркадьй" "облонских -> облонской" Круто!
#######################################################################################

# Посчитаем слова
dict_words = {}
for i in list_text:
    if i in dict_words:
        dict_words[i] += 1
    else:
        dict_words[i] = 1

# Посчитаем лемматизированные слова
dict_normal_words = {}
for i in normal_form_word:
    if i in dict_normal_words:
        dict_normal_words[i] += 1
    else:
        dict_normal_words[i] = 1

# Оба словаря на печать
print(dict_words)
print(dict_normal_words)
print()

# Преведем в список кортежей и отсортируем
list_words_sort = list(dict_words.items())
list_normal_words_sort = list(dict_normal_words.items())

# Чтобы просто посмотреть на все слова, запишем их в файл через "\n"
list_words_sort.sort() # Сортировка по словам
temp = [x[0] for x in list_words_sort]
with open('t4.txt', mode = 'wt', encoding = 'utf-8') as f:
    for i in temp:
        f.write(i)
        f.write('\n')

# И еще хочу посмотреть слова где дефис встречается
for i in temp:
    if '-' in i:
        print(i, end = '; ')
print()

list_normal_words_sort.sort()
for i, ttt in list_normal_words_sort:
    if '-' in i:
        print(i, end = '; ')
print('\n')

# Выведем 5 наиболее часто встречающихся слов
print('Для всех слов:')
list_words_sort.sort(key = lambda x: x[1], reverse = True) # Обратная сортировка по колличеству
for i in range(5):
    print(f'Слово "{list_words_sort[i][0]}" встретилось {list_words_sort[i][1]} раз')

# выведем количество разных слов в тексте
print(f'Всего слов: {len(list_words_sort)}')
print()

# То же самое для лемматизированных слов
# Выведем 5 наиболее часто встречающихся слов
print('Для лемматизированных слов:')
list_normal_words_sort.sort(key = lambda x: x[1], reverse = True) # Обратная сортировка по колличеству
for i in range(5):
    print(f'Слово "{list_normal_words_sort[i][0]}" встретилось {list_normal_words_sort[i][1]} раз')

# выведем количество разных слов в тексте
print(f'Всего лемматизированных слов: {len(list_normal_words_sort)}')