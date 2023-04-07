# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.

my_list = input("Введите числа: ").split( )
print(*my_list)
# print(len(my_list[0]), my_list[0])
# print(len(my_list[1]), my_list[1])
# print(len(my_list[2]), my_list[2])

# def my_filter(same_list):
#     for i in same_list:
#         if  len(i) == 2:
#             return True
#         else:
#             return False
        
my_list = filter(lambda x: len(x) == 2, my_list)
print(*list(my_list))
