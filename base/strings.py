"===========================String===================="
# строки - неизменяемый тип данных, которй предназначен для хранения текста, заключенного в одинарные либо двойные кавычки

string1 = 'строка с одинарнными кавычками'
string2 = "строка с двойными кавычками"
string3 = "Don't" #внутри двойнных кавычек все одинарнные кавычки - просто часть текста
srting4 = 'Название магазина "Азбука"'
string5 = ''' 
Многострчоный текст
в одинарнных кавычках
Тут можно использовать и одинарные и двойные кавычки
'''
string6 = """ 
Много строчный текст 
в двойнных кавычках
Тут можно использовать и одинарные и двойнные кавычки
"""
string7 = 'Привет ' + 'ребята'
# print(string7)

string8 = 'A' * 10 # AAAAAAAAAA
# print(string8)

'==================Экранизация строк================'
'\n' # перенос на новую строку
# print('Hello world') # Hello world
                     

# print('Hello\nworld') #Hello
                        #world

# print('He\llo world') #He
                        #llo world



'\t' # табуляция (несколько пробелов)

# print('Hello\tworld') #hello   world

# print('He\t llo world') #He   lo world



'\v' # перенос на новую строку со смещением вправо на длинну предыдущей строки

#  print('Hello\vworld') #Hello
                         #  world
                         
#  print('Hello\vworld\vmakers') #Hello
                         #          world
                         #               makers




'\r' # перенос каретки в самое начало строки 

#  print('Hello world\rMa') # Mallo world


'\''  # отображение '
"\""  # отображение "

# print('Don\'t') # Don't

'\'' # отоброжение \
#  print('команда \\n - переносит строку')



'=================Форматирование строк============='
#  title = 'IPhone 15'
#  price = 1000
#  shop = 'Makers'
#  print('Я купил title за prise $')

'1. f - строка'

#  print(f'Я купил {title} за {price}$, в магазине {shop}')


'2. %s'

# print('Я купил %s за %s$, в магазине %s' % (title, price, shop))

'3. str.format'

# print('Я купил {} за {}$, в магазине {}' .format (title, price, shop))



'================Методы строк str (string)==============='
# методы - функции, которые относятся к определенному типу данных ( классу), к ним мы обращаемся через точку

#  print(dir(str))



string = "Hello World"
#  print(string.upper()) # HELLO WORLD
#  print(string.lower()) # hello world
#  print(string.swapcase()) # HELLO WORLD

#  print(string.title()) # Hello World
#  print(string.capitalize()) # Hello world

#  print(string.islower()) # True
#  print(string.isupper()) # False



string = "hi"
#  print(string.center(12)) # '     hi     '
#  print(string.center(12, '*')) # *****hi*****



string = "hello world"
#  print(string.count('l')) # 3 
#  print(string.count('el')) # 1
#  print(string.count('o w')) # 1
#  print(string.count('hello')) # 1

#  print(string.startswith('h')) # True
#  print(string.startswith('H')) # False
#  print(string.startswith('hallo')) # False

#  print(string.endswith('ld')) # True
#  print(string.endswith('o')) # False
#  print(string.endswith('ll')) # False



string = 'makers'
#  print(string.isalpha()) # True, проверяет на буквы
#  print(string.isdigit()) # False, проверяет на числа
#  print(string.isalnum()) # True, проверяет на числа и буквы



string = 'hello.world.makers.bootcamp'
#  print(string.split('o')) # ['hell', '.w', 'rld.makers.b', '', 'tcamp']


string = 'hello'
#  print(string.replace('h','m')) #mello
#  print(string.replace('','|')) # h|e|l|l|o|

string = '$$$$$$$$$$$$$$$$hello world$$$$$$$$$$$'
#  print(string.strip('$')) #hello world (убирает все с начала и с конца)

#  ''.join(list) # list это переменная которая хранит тип данных list[]


'===================Индексы==============='
#  Индекс - порядковый номер элемента в последовательности (индекс начинается с 0)

#11-10-9-8-7-6-5-4-3-2-1
#   h e l l o  w o r l d
# 0 1 2 3 4 5  6 7 8 9 10

string = 'hello world'
#  print(string[0]) #'h'
#  print(string[-2]) #'l'
print(string[9]) #'l'

# срез [start:end(не включительно):step]
string[6:10] # world
string[0:-5] # hello
# print(string[::2]) # hlowrd
# print(string[::-1]) # dlrow olleh
# print(string[::-2]) # drwolh





x = int(input())
y = int(input()) 
a = x//y
b = x % y
if x % y != 0: 
     print ('x не делится на y') 
     print ('Частное:', a) 
     print ('Остаток:', b) 
else: 
     print('x делится на y') 
     print('Частное:',a)