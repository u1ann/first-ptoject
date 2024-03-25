'=======================СЛОВАРИ=================='
# dict - изменяемый, итерируемый, неупорядоченный(псевдопорядорк), неиндексируемый тип данных, для хранения даных в парах {ключ: знаение}

# user = {'name':'Anonim', 'age':30, 'last_name':'Makers'}
# print(user['name']) #Anonim
# print(user['age']) #30
# print(user['last_name']) #Makers

# ключами в словаре могут быть только неизменяемые типы данных
# ключи в словаре должны быть уникальными

'============================Создание словарей=========================='
# dict_ = {'a':1, 'b':1}
# dict_ = dict([('a',1),('b',2)])
# print(dict_)

# dict_= dict(['a1', 'b2', 'c3'])
# print(dict_) # {'a': '1', 'b': '2', 'c': '3'}

# dict_ = {}
# dict_['name']='makers'
# dict_['age'] = 50
# dict_['last_name'] = 'bootcamp'
# print(dict_)


'=============================Методы словаря===================='

'get - метод который получает значение по ключу, если указанного ключа нет,то выходит None - по умолчанию, мы можем его поменять'

# user = {
#     'name':'anonym'
#     'age': '35'
#     'last_name': 'makers'}

# print(user['id']) #error - KeyError
# print(user.get('id')) #None
# print(user.get('name', 'Такого ключа нет')) # 'Такого ключа нет'


'pop - удаляет пару по ключу и возвращает значение'
# dict_ = {'a':1, 'b':2, 'c':3}
# popped = dict_.pop('b')
# print(dict_) #{'a': 1, 'c': 3}
# print(popped) #2

'popitem - удаляет последнюю пару и возвращает её'
# dict_ = {'a':1, 'b':2, 'c':3}
# popped = dict_.popitem()
# print(dict_) #{'a': 1, 'b': 2}
# print(popped) #('c', 3)

'update - расширяет словарь парами из второго словаря'

# dict_1 = {1:'a', 2:'a'}
# dict_2 = {2:'b', 3:'b'}
# dict_1.update(dict_2)
# print(dict_1) # {1: 'a', 2: 'b', 3: 'b'}

'clear - очищает словарь'
# dict_ = {'a':1, 'b':2, 'c':3}
# dict_.clear()
# print(dict_) #{}

'fromkeys - метод для создания нового словаря, используя список ключей'

# dict_ = dict.fromkeys('hi')
# print(dict_) #{'h': None, 'i': None}
# dict_2 = dict.fromkeys(['hi', 123, True])
# print(dict_2) #{'hi': None, 123: None, True: None}
# dict_3 = dict.fromkeys(['hi', 123, True], 0)
# print(dict_3) #{'hi': 0, 123: 0, True: 0}

'keys, values, items'
# keys - метод, который возвращает все ключи
# values - метод, который возвращает все значения
# items - метод, который возвращает пары ключ и значение в виде tuple

# user = {
#     'name':'Anonym',
#     'age':15,
#     'last_name':'Makers'
# }
# print(user.keys()) #dict_keys(['name', 'age', 'last_name'])
# print(user.values()) #dict_values(['Anonym', 15, 'Makers'])
# print(user.items()) #dict_items([('name', 'Anonym'), ('age', 15), ('last_name', 'Makers')])

'========================Итерирование словарей======================='

# user = {
#     'name':'Anonym',
#     'age':15,
#     'last_name':'Makers'
# }
# for key in user: 
#     print(key)
# При итерации словаря будут приходить ключи


# for value in user.values(): 
#     print(value)
# При итерации словаря с методом values(), приходят значения


# for item in user.items(): 
#     print(item)
# При итерации с методом items(), приходит tuple с ключем и значением


# for k, v in user.items():
#     print(f'Ключ {k}, значение {v}')
# При итерации словаря с методом items(), приходит tuple с ключем и значением
    
'-------------------------------------------------------------------------------------------------------------------------'
# dict_1 = {1:'a', 2:'b'}
# dict_2 = {}

# for k, v in dict_1.items():
#     dict_2[v] = k

# print(dict_2)

#{'a': 1, 'b': 2}