# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль


def my_fun(**args):
    user_answer1 = int(input('Введите число 1 '))
    user_answer2 = int(input('Введите число 2 '))
    result = user_answer1 / user_answer2
    return result

print(f'result  {my_fun()}')

#if user_answer2 != 0:
#    return user_answer1 / user_answer2
#else:
#    print('Ошибка! Делить на 0 нельзя! ')

# без if не было ошибки - все считалось, добавила стали появляться ошибки. что пошло не так?