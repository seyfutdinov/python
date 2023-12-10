# for i in range() #аргумент stop (до указанного числа)
#     print(i, end = ' ')

# for i in range(3,10) #аргументы start (c указанного числа) + stop (до указанного числа)
#     print(i, end = ' ')

# for i in range(1, 11, 2) #аргументы start (c указанного числа) + stop (до указанного числа)
#     print(i, end = ' ')

# for i in range(10, -1, -1) #реверс последовательности
#     print(i, end = ' ')

# n = 5
# for i in range(n) #реверс последовательности
#     print(i, end = ' ')

# for _ in range(3)
#     print('Hello, my friend')

# for i in range(1, 4)
#     # print(f'Hello, my friend {i+1}')
#     print(f'Hello, my friend {i}')

# num = 0
# for i in range (5)
#     num += 1
# print(num)

# sum = 0
# num = int(input())
# for _ in range(10)
#     sum += num
# print(sum)
#
# # name = input()
# # for _ in range(3)
# #     print(name)

# from random import randint
#
# allEven = 0 #всего четных чисел
# allOdd = 0 #всего нечетных чисел
# positiveEven = 0 #положительных и четных
# negativeOdd = 0 #отрицательных и нечетных
#
# allNumber = 0 #всего чисел
#
#
# for num in range(randint(-100, 0), randint(1, 100))
#     if num % 2 == 0
#         allEven += 1
#         if num  0
#             positiveEven += 1
#     elif num % 2 != 0
#         allOdd += 1
#         if num  0
#             negativeOdd += 1
#     allNumber += 1
#
# print(f'nВ числовой последовательности оказалось всего {allNumber} чисел, из нихn'
#       f'Четных чисел {allEven}n'
#       f'Нечетных чисел {allEven}n'
#       f'Из них:'
#       f'Положительных четных {positiveEven}n'
#       f'Отрицательных нечетных {negativeOdd}n')
#
