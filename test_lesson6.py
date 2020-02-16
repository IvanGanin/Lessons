'''
Light:
1. Выберете дз, к функциям которого будете писать тесты (например, вебинар 5);
2. Создайте дополнительную ветку в репозитории GitHub с тестами;
3. Напишите не менее 5ти тестов к функциям выбранного урока;
4. В качестве ответа на дз пришлите ссылку на ветку с тестами или ссылку на PullRequest ветки с тестами с веткой master.

Pro:

light +
5. Придумайте 2 теста к грязной функции. Примером грязной функции является функция F из задания 4;

'''

fib_num = lambda n: fib_num(n-1)+ fib_num(n-2) if n > 2 else 1
fact = lambda n:1 if n==0 else n*fact(n-1)

with open('log', 'r') as f:
    f = f.readlines()
late_log = max(f, key=lambda x: x[:19])
print(type(late_log))
l=late_log.lower()
print(type(l))

def test_1_fib_num():
    assert fib_num(6) == 8
    assert fib_num(4) <= 8
    assert fib_num(5) != 10

def test_2_fact():
    assert fact(5) == 120
    assert fact(5) != 125

def test_3_open():
   assert l != late_log
   assert type(late_log) == type(l)
