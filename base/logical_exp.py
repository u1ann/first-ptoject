'========================Логические и условные операторы===================='
# boolean - тип данных, который имеет 2 значиения 
# True (Да, истина) и False(нет, и ложь)

# print(bool(0)) #False
# print(bool(-10)) #True
# print(bool(" ")) #True
# print(bool('')) #False
# print(bool(None)) #False


# Логические операторы - выражения, которые возвращают True, если выражение верное, False - если не верное.

'равентство'
5 == 5 #True
5 == 7 #False

'не равенство'
5 != 10 #True
5 != 5 #False

'больше'
5 > 1 #True
0 > 10 #False

'меньше'
10 < 100 #True
0 < -10 #False
5 < 5 #False

'больше или равно'
5 >= 10 #False
10 >= 3 #True
3 >= 3 #True

'меньше или равно'
10 <= 5 #False
5 <= 10 #True
5 <=5 #True




'5' == 5 #False
'hello' == 'hello' #True
'hello' == 'Hello' #False



'=========================And or Not======================='
# and - и
# or - или
# not - не

'AND - возвращает True, если все выражения вернули True'
a = 5
b = 6

#True   и   #True
a == 5 and b == 6 #True

#False  и   #True
a == 6 and b == 6 #False

#True   и  #False
a == 5 and b == 2 #False

#False  и  #False
1 == 1 and b ==1 #False



'OR - возвращает True, если хотя бы один из выражений вернул True, либо когда все выражения вернули True'

c = 5
d = 6

#True или #True 
c == 5 or d == 6 #True

#False или #True
c == 1 or d == 6 #True

#True  или #False
c == 5 or d < 1 #True

#False или #False
c <= 1 or d > 1000 #False



'NOT - это частица не, которая меняет значение на противоположный'

a = 10
b = 5

# not False #True
# not True #False

#not False или #False  и   #True
# not a == b or b > 10 and 10 == a #True

# not not not not not 5 == 5 #False

# not 5 != 5 #True

# bool(None) #False
# bool('None') #True
# bool([]) # False

'========================Условные операторы========================'
# условные операторы - это конструкция которая используется для того чтобы при разных входных данных кот работал по разному (взависимости от условия)

# pagoda = "дождь"
# if pagoda == "дождь":
#    print ('взял зонт')
# elif pagoda == "снег":
#    print ('взял щапку и шарф')
# elif pagoda == 'солнце':
#    print ('взял очки')
# else:
#    print('сижу дома')



# в одной конструкции мы можем использовать только один if
# в одной конструкции мы можем использовать неограниценное кол-во elif или не использовать вообще
# в одной конструкции мы можем использовать только один else или вообще не использовать
   
#Принять от пользователя число, и узнать какое это число, отрицательное, положительное или 0

number = int(input('Введите число: '))

#if number > 0:
   #print('Число положительно')
#elif number < 0:
   #print('Число отрицательно')
#else:
   #print('Число 0')



'=========================Тернарный оператор==========================='
# Тернарный оператор - условия в одну строку

# тело1 if условие1 elso тело2

# num = 10

# if num > 0:
#    message = 'Положительное число'
# else:
#    message = 'Отрицательное число или 0'
# print(message)

# num = 100
# message = 'Положительное число' if num > 0 else 'Отрицательное число'
# print(messgae)






mark = int(input())
if mark >= 90:
  print('Отлично, Ваша оценка 5!')
elif mark >= 80:
  print('Отлично, Ваша оценка 4!')
elif mark >= 70:
  print('Отлично, Ваша оценка 3!')
elif mark >= 60:
  print('Вам стоит подучить материал.')
else:
  print('Вы не сдали экзамен.')


x = 102 
y = 36
z = 90 
print(x if x < y and x < z else y if y < x and y < z else z)