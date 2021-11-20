numbers = list(input("Введите числа через пробел: ").split())

try:
    x = 0
    sum0 = 0
    sum1 = sum0
    ncount = int(len(numbers))
        while x < ncount:
            sum1 = int(numbers[x]) + int(numbers[x + 1]) + sum0
            sum0 = sum1
            x = x + 1
            print("Сумма равна: ", sum1)
except NameError:
    numbers.index(x) == "Q":
    print("Операция завершена. Сумма: ", sum1)









