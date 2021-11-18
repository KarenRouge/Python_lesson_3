def first_func(var_1, var_2):
    return var_1 / var_2


var_us1 = int(input('Введите первое целое натуральное число: '))
var_us2 = int(input('Введите второе целое натуральное число: '))

try:
    first_func(var_us1 / var_us2)
except ZeroDivisionError as Error:
    print("Error")
    var_us2 = int(input("Деление на ноль невозможно. Введите второе целое натуральное число еще раз: "))

print(round(first_func(var_us1, var_us2), 2))
