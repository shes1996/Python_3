# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной
# позиции. Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import math

number = [2, 3, 5, 9, 3, 2, 8, 3]


def sum_odd_position(numbers):
    summary = 0
    for index in range(len(numbers)):
        if index % 2 == 1:
            summary += numbers[index]
    return summary


print(f'Сумма элементов на нечетных позициях равна: {sum_odd_position(number)}')


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д. Пример: - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

def multiplication_pair(numbers):
    multiplication = []
    for index in range(0, len(numbers) // 2 + 1):
        multiplication.append(numbers[index] * numbers[len(numbers) - 1 - index])
    if len(numbers) % 2 == 0:
        multiplication.pop(len(multiplication) - 1)
    return multiplication


print(f'Произведение пар элементов: {multiplication_pair(number)}')

# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

number_float = [1.1, 1.2, 3.1, 5, 10.01]


def diff_max_min_float(numbers):
    float_part = []
    for index in range(len(numbers)):
        if numbers[index] % 1 != 0:
            round_float = round((numbers[index] % 1), 4)
            float_part.append(round_float)
    return max(float_part) - min(float_part)


print(
    f'Разница между максимальным и минимальным значением дробной части из списка {number_float}: {diff_max_min_float(number_float)}')

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = (input('Введите число '))


def decimal_to_binary(number):
    binary_int = ''
    num = int(number)
    while num > 0:
        binary_int += str(round(num % 2))
        num //= 2
    return binary_int[::-1]

#попытка сделать для вещественных чисел
# def float_part_to_binary(number):
#     binary_float = ''
#     num = round(float((number) % 1), 5)
#     while num % 1 != 0:
#         binary_float += str(round((num * 2) % 1))
#         num *= 2
#     return binary_float
#
#
# # print(float_part_to_binary(number))


print(f'Число {number} в десятичной форме является числом {decimal_to_binary(number)} в двоичной форме')

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = 8


def fibonachi(number):
    fibo = []
    negafibo = []
    for index in range(0, number + 1):

        if index == 0:
            fibo.insert(0, 0)
        elif index == 1:
            fibo.insert(1, 1)
        else:
            fibo.insert(index, fibo[index - 2] + fibo[index - 1])
    for index in range(1, number + 1):
        if index % 2 == 0:
            negafibo.insert(0, fibo[index] * -1)
        else:
            negafibo.insert(0, fibo[index])
    return negafibo+fibo


print(f'Список чисел Фибоначчи до {number}го числа: {fibonachi(number)}')
