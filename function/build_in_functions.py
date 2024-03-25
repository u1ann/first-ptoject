'=======================Встроенные функции====================='

#map, filtre,reduse,zip,enumerate
'ZIP - соединяет несколько последовательностей (получаем генератор в котором элементы - tuple)'

# list1 = [1,2,3,4]
# list2 = ['a', 'b', 'c', 'd']
# list3 = [10.5, 20.6, 35.8, 0.5]

# zipped = zip(list1, list2, list3)
# print(list(zipped)) list[tuple, tuple, tuple]
# print(dict(zipped)) dict{k:v, k:v, k:v}

'ENUMERATE'
# нумерует последовательность (по дефольту с 0) (тоже возвращает генератор)

# enumerated = enumerate('hello') # <enumerate object at 0x7accd2f8bf00>
# print(enumerated)
# print(list(enumerated)) [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
# print(list(enumerated)) [(699, 'h'), (700, 'e'), (701, 'l'), (702, 'l'), (703, 'o')]

# for i in enumerated:       
#     print(i)

# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')
    
enum = enumerate([12, 8, 'hi', True, 'HELLO', None, 15]) #[(15, 12), (16, 8), (17, 'hi'), (18, True), (19, 'HELLO'), (20, None), (21, 15)]
# print(list(enum))

# for n, v in enum:
#     print(f'Номер: {n}, Значение: {v}')

# Номер: 0, Значение: 12
# Номер: 1, Значение: 8
# Номер: 2, Значение: hi
# Номер: 3, Значение: True
# Номер: 4, Значение: HELLO
# Номер: 5, Значение: None
# Номер: 6, Значение: 15

'MAP'
# принимает другую функцию и последовательность, мэп применяет функцию, которую передали на каждыф элемент из последовательности. Возвращает map объект

# list_ = [1,2,3,4]
# def func(a):
#     return str(a)

# mapped = map(func, list_)
# print(mapped) # <map object at 0x7e0cc351bd30>
# print(list(mapped)) # ['1', '2', '3', '4']


# list_1 = [1,2,3,4] # ->  [1, 4, 9, 16]
# def func(a):
#     return

# mapped = map(func, list_1)
# print(list(mapped))


'lambda - это одноразовое, анонимная функция'

# def func(num1):
#     return num1 ** 3

# func(2) # 8


# result = lambda num1:num1 ** 3
# print(result(2))

# list_1 = [1, 2, 3, 4]
# mapped = map(lambda x: x ** 2, list_1)
# print(list(mapped)) #[1, 4, 9, 16]


'FILTER'
# принимает другую функцию и последовательность, применяет функцию, которую  мы передали на каждый элемент последовательности и оставляет только те элементы, которые прошли проверку

# list_1 = [-10, 0, 39, -12, -3, 23, 1, 0] # ->
# # [0, 39, 23, 1, 0]

# def func(a):
#     return a >= 0

# filtered = filter(func, list_1)
# print(list(filtered)) # [0, 39, 23, 1, 0]

# filtered = filter(lambda a: a >= 0, list_1)
# print(list(filtered)) # [0, 39, 23, 1, 0]

# list_1 = [1,2,3,4,5,6,7,8]
# filtered = list(filter(lambda x: x % 2 == 0, list_1))
# print(list(filtered)) # [2, 4, 6, 8]

'REDUCE'
# принимает функцию и последовательность, возвращает 1 результат (передаваемая функция, должна принимать 2 аргумента)

from functools import reduce

# list_1 = [12, 3, 0, 5]
# print(reduce(lambda a, b: a + b, list_1)) # 20


