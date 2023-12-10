# num = int(input('Введите число: '))
# num = str(num)
# print(f'В числе - {len(num)} символ(а)ов')
# print('Сумма двух чисел =', num + str(10) )

# while True:
#     print(str('Загрузка...'))

# while True:
#      print(int(99))
#      break

# while False:
#      print(int(99))


# while True:
#     num = int(input('Введите число: '))
#     if num == 27:
#         print(f'Вы ввели число {num}')
#         break
# else:
#     print('Вы ввели неправильное число')

# while True:
#     code = str(input('Кодовое слово: '))
#     if code == 'Сосиска':
#         print('Активировано!')
#         break
#     else:
#         print('Не активировано! Попробуйте ещё!')

# while True:
#     code = str(input('Кодовое слово: '))
#     if len (code) == 5:
#         print('Вы ввели слово нужной длины!')
#         break

# num = 1234
# if num // 1000 % 2 == 0:
#     print('Первая цифра этого числа является чётной')
# else:
#     print('Первая цифра этого числа является нечётной')

# while True:
#     lang = str(input('Язык программирования из 6 букв: '))
#     if len(lang) > 0:
#         print('Данные введены')
#         if len(lang) == 6 and lang == 'python':
#             print('Вы угадали загаданное слово!')
#             break
#     else:
#         print('Данные отсутствуют')

# while True:
#     word = input('Язык программирования из 6-ти букв: ').lower()
#     if word == '':
#         print('Вы ничего не ввели\n')
#     elif len(word) == 6 and word == 'python':
#         print('Правильно!')
#         break
#     else:
#         print('Ответ не верный\n')

# while True:
#     answer = input('Нравится ли тебе твоя зарплата? ').lower()
#     if answer == 'да':
#         print('Отлично! Я так и думал…')
#         break
#     else:
#         print('Еще раз')

# while True:
#     num = int(input('Введите число: '))
#     if num % 5 == 0 and num % 2 == 0:
#         print(f'Число {num} делится на 2 и 5')
#         break
#     else:
#         print('Попробуйте ещё')


# while True:
#     num = int(input('Введите число: '))
#     if num % 2 == 0 or 10 <= num <= 20 :
#         print(f'Число {num} входит в диапазон')
#         break
#     else:
#         print('Попробуйте ещё')


# while True:
#     slovo = str(input('Введите строку: '))
#     if len(slovo) <= 5 and 'а' in slovo:
#         print(f'Строка {slovo} введена верно')
#         break
#     else:
#         print('Попробуйте ещё')


# while True:
#     old = int(input('Введите ваш возраст: '))
#     pravo = input('Есть ли у вас права?(Да / Нет): ').lower()
#     if old >= 18 and pravo == "да":
#         print('Вы имеете право сесть за руль')
#         break
#     else:
#         print('Вы не имеете права садиться за руль')
#         break

# while True:
#     old = int(input('Введите ваш возраст: '))
#     grazhd = input('Есть ли у вас гражданство РФ?(Да / Нет): ').lower()
#     if old >= 18 and grazhd == "да":
#         print('Вы имеете право пойти на выборы')
#         break
#     else:
#         print('Вы имеете не права пойти на выборы')

# while True:
#     num = int(input('Введите число: '))
#     if num % 3 == 0 and num % 5 == 0 and num % 10 != 0:
#         print(f'Число {num} входит в диапазон')
#         break
#     else:
#         print('Попробуйте ещё')