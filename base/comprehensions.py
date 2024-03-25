'==========================Comprehensions==============='
# генератор с помощью которого можно создать последовательность используя for в одну строку
#результат for элемент in последовательность
# list_1 =[x + 2 for x in range(11)]
# print(list_1) #[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# list1 = []
# for i in range(1,11):
#     if i % 2 == 0:
#         list1.append(i)
# print(list1)

# list_ = []
# for i in range(1,11):
#     if i % 2 == 0:
#         list_.append('четный')
#     else:
#         list_.append('нечетный')
# print('list_')


# list_ = ['четный' if i % 2 == 0 else 'нечетный' for i in range(1,11)] #['нечетный', 'четный', 'нечетный', 'четный', 'нечетный', 'четный', 'нечетный', 'четный', 'нечетный', 'четный']
# print(list_) #['нечетный', 'четный', 'нечетный', 'четный', 'нечетный', 'четный', 'нечетный', 'четный', 'нечетный', 'четный']

'В comprehension можно добавить условия, там их бывает 2 вида'
'1 - тернарный оператор, пишется перед циклом, так как используем и if и else'
'2 - фильт, пишется после цикла, так как испоьзуется только if'

# Создать список из сущесствующего списка, оставив только строки
# list_1 = [2, True, None, 'hi', 0, False, 'makers', 'world']

# list_2 = [i for i in list_1 if type(i) ==str]
# print(list_2 )

# a = 12
# print(type(a==int)) #True

'================================================Виды comprehension=============================='
'1 - list comprehension'
'2 - list comprehension'
'3 - list comprehension'

'Dict comprehension'
# dict_1 = {i:i for i in range(1,11)}
# print(dict_1) # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}


'Дан словарь dict_1 поменяйте ключи и значения с помоьщю comprehension'
# dict_1 = {'a':1, 'a':1, 'b':2, 'c':3}
# dict_2 = {value: key for key, value in dict_1.items()}
# print(dict_2) #{1: 'a', 2: 'b', 3: 'c'}


'Дань словарь где значения - списки из чисел, создайте словарь, где значения будут суммы этих списков'
# dict_1 = {
#         'a':[1,2,3],
#         'b':[12,0,1],
#         'c':[32,0, 0, 10]
# }

# sum_dict = {key: sum(value) for key, value in dict_1.items()}
# print(dict_1)
# print(sum_dict)


'Set comprehension'

# set_1 = {i for i in range(1,11)}
# print(set_1)

# set_1 = {i for i in 'makers'}
# print(set_1)

# set_1 = {2, 3, 4, 15, 1}
# set_2 = {i**2 for i in set_1}
# print(set_2) #{1, 225, 4, 9, 16}

# set_2 = {i**i for i in set_1}
# print(set_2) #{256, 1, 4, 437893890380859375, 27}

# set_1 = {12, 4, 34,5, 6}
# set_2 = {str(i) for i in set_1} #{'5', '12', '6', '34', '4'}
# print(set_2)

# "сохранить только строки"
# set_1 = {1, 12, 'hi', 34, True, 'makers'}
# set_2 = {i for i in set_1 if type(i) == str} #{'hi', 'makers'}
# print(set_2)

# "Сохраните только строки, те строки в которых хранятся числа переведите с int '12' -> 12, а простые строки с символами и буквами сохраните"
# set_1 = {12, True, 'hi', 23, '10', 'makers', False, '1'}
# set_2 = {}

# 'СОздайте словарь, где ключи будут числа от 1 до 5, ф значениями - списки с числами от 1 до этого числа'
# dict_1 = {i: [i for i in range(1,i+1)] for i in range (1,6)} # {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}
# print(dict_1) 

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list = max(lists, key=len)
# min_list = min(lists, key=len)
# print("max_list", max_list)
# print("min_list", min_list)

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# lengths = [] 
# for i in lists: lengths.append(len(i)) 
# print(f'max_list {lists[max(lengths)+1]}') 
# print(f'min_list {lists[min(lengths)-1]}')

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# lists = [ [13],[13]] 
# max_ = max([x for x in lists], key=len)
# min_ = None
# if len(lists) > 1:
#     min_ = min([x for x in lists],key=len)
# if max_ == min_: 
#     min_ = None
# print(f'max_list {max_}') 
# print(f'min_list {min_}')

# a = {'x': 1, 'y': 2, 'z': 1} 
# print(list(a.keys())[0])

inp1 = input() 
inp2 = input() 
inp3 = input() 
inp4 = input() 
inp5 = input()
list0 = [] 
list0.append(inp1)
list0.append(inp2) 
list0.append(inp3) 
list0.append(inp4) 
list0.append(inp5) 
list1 = [] 
target = ' ' 
for i in list0: 
    t = i.find(target) 
    r = i.rfind(target) 
if i.count(target) > 1: 
    list1.append(i[r+1:]) 
else: 
    list1.append(i[t+1:]) 
print(sorted(list1))



surnames = []
for _ in range(5):
    full_name = input()
    surname = full_name.split()[-1]
    surnames.append(surname)
    surnames.sort()
print()
for surname in surnames:
    print(surname)

