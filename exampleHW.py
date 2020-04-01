# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# i = 5
# while i < 6:
#     print('Строка №1 0')
#     print('Строка №2 0')
#     print('Строка №3 0')
#     print('Строка №4 0')
#     print('Строка №5 0')
#     i = i+2
#     if i==7: break
#
# for i in ['№1 0', '№2 0','№3 0','№4 0','№5 0']:
#    print(i)


'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# count_five = 0
# for i in range(10):
#     digit = int(input('Введите цифру'))
#     if digit == 5:
#       count_five = count_five + 1
#     print("Количество пятерок", count_five)





'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

#
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# mult = 1
# for i in range(1,10):
#     mult *=i
# print(mult)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number > 0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# number = int( input('input number:'))
# sum = 0
# while number > 0:
#     i = number % 10
#     number = number // 10
#     sum = sum + i
# print('Summury is', sum)


'''
Задача 7
Найти произведение цифр числа.
'''
# multi = 1
# number = int( input('Input number:'))
# while number > 0:
#     i = number % 10
#     number = number // 10
#     multi = multi * i
# print('Multi is', multi)



'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# a = int(input('Введи число:'))
# m = a%10
# a = a//10
# while a > 0:
#    if a%10 > m:
#        m = a%10
#    a = a//10
# print(m)

'''
Задача 10
Найти количество цифр 5 в числе
'''
#
# count_five = 0
# d = int(input('Введите цифру'))
# while d > 0:
#     if d%10 == 5:
#        count_five = count_five + 1
#     d = d // 10
# print ('Количество цифр 5 в цисле:', count_five)


