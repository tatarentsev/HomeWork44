# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

first_set = {1, 25, 7, 11, 8, 0, 3, 2, 4}
second_set = {32, 4, 36, 8, 0, 53, 3, 7}

set_union = first_set.union(second_set)
print(sorted(set_union))