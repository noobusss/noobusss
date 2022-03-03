#              ***********Урок 1 Домашнее задание 1***********

# name = input("Введите ваше имя: ")
# print(f"Здравтсвуйте {name}")


#              ***********Урок 1 Домашнее задание 2***********

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
#
# numsum = num1 + num2 + num3
#
# print(f"Ваше число {numsum}")


#              ***********Урок 1 Домашнее задание 3***********

# schooler = input("Введите количество школьников: ")
# apple = input("Введите количество яблок: ")
#
# if not schooler or not apple:
#     print("Кажется вы забыли ввсети данные")
# elif not schooler.lstrip().isdigit() or not apple.lstrip().isdigit():
#     print("Кажется вы указали не полные числа")
# elif int(apple) < 0 or int(schooler) < 0:
#     print("Не могу посчитать")
# else:
#     quantity = int(apple) // int(schooler)
#     basket = int(apple) % int(schooler)
#     print (f"Каждому школьнику достанется {quantity} яблок")
#     print(f"В корзине останется {basket} яблок")


#              ***********Урок 1 Домашнее задание 4***********

# print("""Twinkle, twinkle, little star,
#     How I wonder what you are!
#         Up above the world so high,
#         Like a diamond in the sky.
#     Twinkle, twinkle, little star,
#         How I wonder what you are""")
# print('''Twinkle, twinkle, little star,
#     How I wonder what you are!
#         Up above the world so high,
#         Like a diamond in the sky.
#     Twinkle, twinkle, little star,
#         How I wonder what you are''')
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are!  \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star,\nHow I wonder what you are")


#              ***********Урок 1 Домашнее задание 5***********
# number = input("Введите число: ")
#
# if not number or not number.lstrip("-").isdigit():
#     print("Введите целое число")
# else:
#     next_number = int(number) + 1
#     previous_number = int(number) - 1
#     print(f"Следущее число для {number} - {next_number}")
#     print(f"Предыдущее число для {number} - {previous_number }")


#              ***********Урок 1 Домашнее задание 6***********

# totalMoney = 1000
# quantity = 3
# price = 450
#
# print(f"Уменя есть {totalMoney} долларов,поэтому я могу купить {quantity} футбольных мяча за {price} долларов")


#              ***********Урок 2 Домашнее задание 1***********

# age = input("Ваш возраст: ")
#
# if not age or not age.lstrip("-").isdigit():
#     print("Указаны не верные данные, укажите в числовом формате")
# elif 0 < int(age) <= 18:
#     print("Вам нужно учиться.")
# elif 18 < int(age) <= 50:
#     print("Вам нужно работать.")
# elif 50 < int(age) <= 59:
#     print("Вам скоро на пенсию.")
# elif  59 < int(age) <= 110:
#     print("Вы персионер.")
# else:
#     print("Вам больше нельзя играть в лего :(")

#              ***********Урок 2 Домашнее задание 1***********
# month = input("Введите номер месяца: ")
#
# month = input("Введите номер месяца: ")
#
# if not month or not month.lstrip("-").isdigit():
#     print("Не верные данные, повторите попытку")
# elif  int(month) < 1 or int(month) > 12 :
#     print(f"Месяца под номером '{month}' не бывает")
# elif int(month) == 1:
#     print("Название месяца: Январь. Количество дней: 31")
# elif int(month) == 2:
#     print("Название месяца: Февраль. Количество дней: 28")
# elif int(month) == 3:
#     print("Название месяца: Март. Количество дней: 31")
# elif int(month) == 4:
#     print("Название месяца: Апрель. Количество дней: 30")
# elif int(month) == 5:
#     print("Название месяца: Май. Количество дней: 31")
# elif int(month) == 6:
#     print("Название месяца: Июнь. Количество дней: 30")
# elif int(month) == 7:
#     print("Название месяца: Июль. Количество дней: 31")
# elif int(month) == 8:
#     print("Название месяца: Август. Количество дней: 31")
# elif int(month) == 9:
#     print("Название месяца: Сентябрь. Количество дней: 30")
# elif int(month) == 10:
#     print("Название месяца: Октябрь. Количество дней: 31")
# elif int(month) == 11:
#     print("Название месяца: Ноябрь. Количество дней: 30")
# elif int(month) == 12:
#     print("Название месяца: Декабрь. Количество дней: 31")


# ## 3. Написать программу, которая спрашивает у пользователя три числа и выводит количество совпадающих.
# print("## Урок второй, домашнее задание №3")
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
#
# if num1 == num2 == num3:
#     print("Кол-во совпадающих чисел: 3")
# elif  num1 == num2 or num1 == num3 or num2 == num3:
#     print("Кол-во совпадающих чисел: 2")
# else:
#     print("Кол-во совпадающих: 0")

#
#
## 4. Если заданы два целых числа, они возвращают свое произведение только в том случае, если произведение не больше 1000, иначе возвращают свою сумму.
# print("## Урок второй, домашнее задание №4")
#
# num1 = input("Введите первое число: ")
# num2 = input("Введите второе число: ")
#
# if not num1.lstrip("-").isdigit() or not  num2.lstrip("-").isdigit():
#     print("Вы ввели не числовое значение")
# else:
#     result = int(num1) * int(num2)
#     if result <= 1000:
#         print(f"Результат {result}")
#     else:
#         result = int(num1) + int(num2)
#         print(f"Результат {result}")
# print("_"*50)
#
# ## 5. Напишите программу для отображения «Hello», если введенное пользователем число кратно пяти, в противном случае выведите «Bye»
# print("## Урок второй, домашнее задание №5")
# number = input("Введите любое число: ")
#
# if not number.lstrip("-").isdigit():
#     print("Вы ввели не числовое значение")
# else:
#     remainder = int(number) % 5
#     print("Hello") if remainder == 0 else print("Bye")
# print("_"*50)
#
#
# ##  6. *Написать программу, которая спрашивает у пользователя год и определяет является ли год високосным.В соответствии с григорианским календарем, год является високосным,если его номер кратен 4, но не кратен 100 или кратен 400.
# print("## Урок второй, домашнее задание №6")
# year = input("Введите произвольный год: ")
# if not year.isdigit():
#     print("Вы ввели не правильный год")
# else:
#     if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
#         print(f"{year} год  имеет 366 суток в году и является високосным годом.")
#     else:
#         print(f"{year} год  имеет 365 суток в году и НЕ является високосным годом.")
# print("_"*50)
#
#
# ## 7. *Шоколадка имеет вид прямоугольника, разделенного на width×length долек.
# print("## Урок второй, домашнее задание №7")
# width = input("Введите width: ")
# length = input("Введите length: ")
# parts = input("Введите parts: ")
#
# if not width.isdigit() or not length.isdigit() or not parts.isdigit():
#     print("Вы указали не верные параметры")
# else:
#     width = int(width)
#     length = int(length)
#     parts = int(parts)
#     if parts < width * length and ((parts % width == 0) or (parts % length == 0)):
#         print('YES')
#     else:
#         print('NO')
# print("_"*50)
# print ("Усё :)")
# input ("Нажмите Enter чтоб завершить код")
