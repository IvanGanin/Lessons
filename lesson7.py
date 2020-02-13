#import csv
import json


from timeit import timeit

'''
LIGHT:

1) Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).
2) Создать doc шаблон, где будут использованы данные параметры.
3) Автоматически сгенерировать отчет о машине в формате doc (как в видео 7.2).
4) Создать csv файл с данными о машине.
5) Создать json файл с данными о машине.

PRO:
LIGHT +
6) Замерить время генерации отчета (время выполнения пункта 3). В каждый файл пунктов 4 и 5
добавить параметр: время, затраченное на генерацию отчета.
'''

FILENAME = 'text.csv'
with open(FILENAME, encoding='cp1251') as file:
    car_list = [row for row in csv.DictReader(file)]

for row in car_list:
    print(row)
print()

# генерируем отчет в docx
#context = {
 #   'my_title': 'Список авто',
  #  'my_list': [i['Производитель'] + ' - ' + i['Модель'] + ' ' + i['расход топлива'] + '-' + i['стоимость'] for i in car_list[:-1]]
#}

print(context)
'''
# Время, затраченное на генерацию отчета
# Чтобы его измерить, нам нужна строка кода в строковой переменной.
code_string = "doc = DocxTemplate('template.docx'); doc.render(context); doc.save('Список машин.docx')"
repeats = 1  # Если захотим сделать несколько замеров для точности)
time = timeit(code_string, number=repeats, globals=globals()) / repeats
print(time)

title = tuple(k for k in car_list[0])
data = [tuple(d.values()) for d in car_list]
'''