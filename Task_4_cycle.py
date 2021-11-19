def my_func(x, y):
    for x in range (1,y):
        result = x * x
    return result

x1 = int(input("Введите первое число: "))
y1 = int(input("Введите второе число: "))
print(f"Результат: {my_func(x1, y1)}.")


