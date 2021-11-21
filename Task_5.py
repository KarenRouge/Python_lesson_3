def sum():
    x = 0
    while True:
        numbers = input("Введите числа через пробел. Для выхода нажмите 'q':").split()
        for i in numbers:
            if i == 'q':
                return x
            else:
                x += int(i)

        print("Сумма введенных чисел: ", x)


print(sum())
