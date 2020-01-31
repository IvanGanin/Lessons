with open('text.txt', mode = 'rt', encoding = 'utf-8') as f:
    text = f.read()

'''
1) методами строк очистить текст от знаков препинания;
'''
temp = set()
for i in text:
    temp.add(i)
temp.remove(' ')
temp.remove('\n')
ltemp = list(temp)
ltemp.sort()
ltemp = ['['] + ltemp + [']'] # А вдруг что-то непечатное, типа табуляции, в начале или в конце строки
print(*ltemp, sep = '')

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

for i in punctuation:
    text = text.replace(i, ' ')


'''
2) сформировать list со словами (split);
'''
words = text.split()
print(words)


'''
3) привести все слова к нижнему регистру (map);
'''

temp = list(map(lambda x: x.lower(), words))
list_text = [i.lower() for i in words]
print(list_text)


'''
3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
'''

dict_words = {}
for i in list_text:
    if i in dict_words:
        dict_words[i] += 1
    else:
        dict_words[i] = 1

print(dict_words)




'''
4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
'''
list_words_sort = list(dict_words.items())

print('Для всех слов:')
list_words_sort.sort(key = lambda x: x[1], reverse = True) # Обратная сортировка по колличеству
for i in range(5):
    print(f'Слово "{list_words_sort[i][0]}" встретилось {list_words_sort[i][1]} раз')


'''
PRO:
5) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.
'''
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

normal_form_word = [morph.parse(i)[0].normal_form for i in list_text] # Опять же, можно было map()
del morph

print(normal_form_word)
print()

dict_normal_words = {}
for i in normal_form_word:
    if i in dict_normal_words:
        dict_normal_words[i] += 1
    else:
        dict_normal_words[i] = 1

print(dict_normal_words)
dict_normal_words = {}
for i in normal_form_word:
    if i in dict_normal_words:
        dict_normal_words[i] += 1
    else:
        dict_normal_words[i] = 1

list_words_sort = list(dict_words.items())
list_normal_words_sort = list(dict_normal_words.items())

list_normal_words_sort.sort()
for i, ttt in list_normal_words_sort:
    if '-' in i:
        print(i, end = '; ')

print(normal_form_word)



f.close()
