'=======================List========================='
# списки - изменяеммый, индексируемый, упорядоченный, интерируемый тип данных, предназначенный для хранения любых данных в определенном порядке

# list_1 = [1, 2, 14, 'Hello', True, [0,0,0], None]
 #Индексы 0  1  2     3       4       5      6

# list_1[3] # 'Hello'
# list_1[-1] # None
# list_1[-2][-1] # 0
# list_1[3][-2] # l
# list_1[5] # [0,0,0]

'range(start, end( включительно), step) - это функция генератора, которая генерирует\создает диапазон от start до end(не включительно)'

#list_1('Hello') -> ['h', 'e', 'l', 'l', 'o']
# list_2 = list(range(0, 101)) # [0, 1, 2, 3 ........,99, 100]
# print(list_2)
# print(list(range(50,71)))
# print(list(range(0, 11, 2))) # [0, 2, 4, 6, 8, 10]
# print(list(range(0, 11))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(range(11, 4, -1))) #[11, 10, 9, 8, 7, 6, 5]

'============================Методы списков================='
'append - добавление элемента в конец списка'

# list_ = []
# list_.append(1)
# list_.append('hello world')
# list_.append(True)
# print(list_) # [1, 'hello world', True]

'pop - удаление элемента из списка по индексу, возвращает удаленный элемент. Если не указать индекс, то удалить с конца '

# list_ = [90, True, None, 'Hi']
# popped = list_.pop(1)
# print(list_) # [90, None, 'Hi']
# print(popped) # [True]

'remove - это удаление элемента из списка по значению'

# list_ = [1, 2, 3, 5, 99, 0, -11]
# list_.remove(5)
# print(list_)


'count - считает кол-во принятого элемента в списке'

# list_ = [1, 23, 1, 4, 5, 'hi', 6, 1, 7, 1, 7, 8, 1, 'hi']
# print(list_.count(1)) #5
# print(list_.count(7)) #2
# print(list_.count('hi')) #2

'index - возвращает индекс первого вхождения принятого элемента'

# list_ = ['hi, 1, 341, 2, 0, 2, 1, 99, 10']
# print(list_.index('hi')) #0



'extend - расширяет список при помощи другого списка'

# list_1 = [1, 2, 3]
# list_2 = [0, 0, 0]
# list_1.append(list_2) #[1,2,3,[0, 0, 0]]
# print(list_1)
# list_1.extend(list_2) #[1,2,3,[0,0,0],0,0,0]
# print(list_2)


'reverse - изменяет список, расставляя его элементы в обратном порядке'

# list_ = ['hi', 1, 2, 3, True]
# list_.reverse()
# print(list_) # [[1,2,3], True, 3, 2, 1, 'hi']


'sort - сортирует список, состоящий из элементов одно типа данных'

# list_ = [12, 4, 1, 0, 25, 7]
# list_.sort()
# print(list_)

# list_ = ['c', 'b', 'a', 'A', 'B']
# list_.sort()

# print(list_)


'clear - очищает список'

# list_ = [12, 42, 34, 3, 4, 56]
# list_.clear()
# print(list_) #[]


'ожественное присвоение'

# a, b , c = 10, 5, 2
# print(a, b, c)


list_ = [23, 14, 'hi', 4, 0, 'makers']

for i in list_:    
    print(i)
# 23
# 14
# hi
# 4
# 0
# makers
    
meshok = ['картошка', 'лук','лук', 'картошка', 'лук', 'морковка']

paket1 = []
paket2 = []
paket3 = []

for ruka in meshok:
    if ruka == 'картошка':
        paket1.append(ruka)
    elif ruka == 'лук':
        paket2.append(ruka)
    elif ruka == 'морковка':
        paket3.append(ruka)


print(paket1)
print(paket2)
print(paket3)

