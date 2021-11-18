def my_func(Var_1, Var_2, Var_3) :
    sum = Var_1 + Var_2 + Var_3
    return sum

number_list = list(input("Введите 3 числа через пробел: ").split())
number_list.remove(min(number_list))
var1_u = int(number_list[0])
var2_u = int(number_list[1])
print(my_func(var1_u, var2_u, 0))







