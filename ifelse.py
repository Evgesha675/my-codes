'''# if - если 
# else - иначе
# cпрашиваем возраст пользователя (с клавиатуры вводим число)
Age = int(input("Сколько вам годиков?: "))
#  если возраст больше или равен 18 
if Age >= 18:
# выводим это
    print("Вы совершеннолетний!!!")
# иначе
else: 
# выводим это
    print("Вы ещё дитё")
    '''
'''
integer = int(input())
if integer > 0: 
    print("Число положительное")
elif integer < 0: 
    print("Число отрицательное")
else: 
    print("Число равно нулю")
   '''
'''
a = int(input())
if a%1==0 and a%a==0 and a%6==0:
    print(f'Число {a} делится на 1 и на само себя')
else:
    print(0)'''

# написать программу, которая определяет високосный год или нет
# Год делится на четыре без остатка. 
# Если год делится на 100 (годы оканчиваются двумя нулями, например, 1900, 2100), это не високосный год, за исключением случаев из условия 3.
# Если год делится на 400 — он високосный. 
'''
integer = int(input())
if integer % 4==0:
    print("год високосный")
elif integer % 100==0:
    print("не високосный")
elif integer % 400==0:
    print("год високосный")
else: 
    print("не високоснный")'''
'''
year = int(input())
if year%4==0 and year%400: print("Вискосоный")
else: print("не високосный")
'''


# # Практическое задание 1:
# Напишите программу, которая:

# Запрашивает у пользователя его имя и возраст.
# Если возраст меньше 18 лет, выводит: "Привет, [имя]! Ты еще подросток."
# Если возраст 18 и больше, выводит: "Привет, [имя]! Добро пожаловать во взрослую жизнь."

