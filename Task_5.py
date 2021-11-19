def my_func():
    number_list = (input("Введите несколько чисел через пробел: ")).split()
    try:
        sum(number_list)
    except NameError as Err:
        print(Err, "Операция завершена")
    return sum


print(sum)
