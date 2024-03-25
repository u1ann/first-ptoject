'========================================Области видимости==============================================='
# LEGB - local enclosed global build-in
'Build-in(Встроенная пространство)'
# Это пространство, которое находится в python (print, input, int, str, sum)

'Global(Глобальное пространство)'
# Это пространство, которое находится  вас в файле
# globals() -  показывает все глобальные переменные
# a = 5
# b = 'hello'
# print(globals())

'Enclosed(Замкнутое пространство)'
# Это пространство, которое находится во вложенных функциях
# var = 'global'
# def func():
    # локальное пространство для глобального пространство
    # замкнутое пространство (потомучто есть более локальное пространство)
#     var = 'local'
#     def func2():
#         #  локальное пространство для пространства func
#         var = 'local'
#         print(var)
#         func2()

# print(var)
# func()

'Local(Локальное пространство)'
# Это пространство, которое находится внутри функции
# locals() - выводит переменные локального пространства
# a = 18

# def func(a, b):
#     print(a, b)
#     print('Глобальное', globals())
#     print('Локальное', locals())

# func(0, 1)

'global - это оператор, который позволяет менять переменную с глобального пространства' 


# var = 'global'
# def func():def func17(employees): return [{'name': emp['name'], 'salary': emp['salary'] + emp['overTime'] * 200} for emp in employees] employees = [ {'name': 'Jack', 'salary': 10000, 'overTime': 4}, {'name': 'Tom', 'salary': 15000, 'overTime': 3}, {'name': 'Jessica', 'salary': 20000, 'overTime': 9}, {'name': 'Helen', 'salary': 25000, 'overTime': 2}, {'name': 'Peter', 'salary': 30000, 'overTime': 7} ] result = func17(employees) print(result)

#     var = 10


# print(var)
# func()
# print(var)



# def func():
#     var = 'enclosed'
#     def func2():
#         nonlocal var
#         var = 'local'
#     print(var)
#     func2()
#     print(var)


# func()

'nonlocal - это оператор, который позволяет менять переменную с не локального пространства'
'--------------------------------------------------------------------------------------------------------------------------------------'

# Напишите функцию которая увеличевает глобальную переменную count

# count = 0

# def incr():
#     global count
#     count += 1

# incr()
# incr()
# incr()
# incr()
# incr()
# print(count)  #5




def foo(): 
    var = 'переменная foo' 
    print('переменная в foo: ', var) 
def bar(): 
    global var 
    var = 'переменная bar' 
    bar() 
    foo() 
    print('переменная в foo: ', var)