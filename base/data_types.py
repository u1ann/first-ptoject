'==================ПЕРЕМЕННЫЕ======================='
#  Переменнные  - это ссылки на ячнйку памяти, где хранятся какие-то данные для дальнейшего использования этих данных.

num1 = 10
num2 = 55
num3 = 10
print(num1 + num2 - num3)

'---------Правила наименования переменных============'
# a = 5 # можно, но назначение не понятное
# # 1num = 10 cntrl + / # нельзя использовать переменные с числа
# my name = 'Makers' # нельзя использовать пробелы
# my-name = 'Makers' # нельзя использовать символы кроме (_)

# print = 'Makers' # нельзя использовать встроенные названия функций, команд, операторов

# имя = 'Makers' #  нельзя писать названия кириллицей


# Snake Case - python  стиль наименования переменных
my_name = 'makers'

# Camel Case -  стиль остальных языков программирования
myName = 'makers'

'============Ввод и вывод данных=========='
# print - функция вывода данных в терминал
# input - функция ввода данных с терминала

# number = input('Введите число: ')
# print(number)

'==============Типы данных============'
# Типы данных в питоне делятся на 2:
# Изменяемые и неизменяемые

# 'Изменяемые'
# list
# set
# dict

# 'Неизменяемые'
# int, float, decimal, complex
# str 
# tuple
# bool
# None
# frozenset


'===============Integer============='
# int -  целые числа (15)
# float - числа с плавающей точкой (15.9)
# decimal - числа с плавающей точкой, но с большим диапозоном чисел после точки (15.9012042010)
# complex - числа из выс.математики (5j)

# num1 = 10
# num2 = 0.5
# print(num1 + num2)

num1 = '10'
num2 = 10
print(int(num1)+10)

#int() - функция int  переводит текст с числом в тип данных число

'=================Операции над числами==============='

# 10 + 10 = 20 - сложение
# 10 - 10 = 0 - вычитание
# 10 * 10 =100 - умножение
# 10 / 5 =2.0 - деление с запятой
# 10 // 5 = 2 - деление целочисленное
# 10 % 3 = 1 - остаток от деления
# 10 ** 2 = 100 - возвездие в степень

import math
print (math.pi)

