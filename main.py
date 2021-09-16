# PROBLEM 12
#
# Создать список и 5 вложенных кортежей.

# x = 0
# y = [5, 7, 11, 12, 13, 14]
# z = 2
# list1 = [(x, item, z) for item in y]
# print(list1)




# PROBLEM 32
#
# Создать Tuple из 3 элементов и вывести каждый из них по индексу.
# def del_from_tuple(tpl, elem):
#     lst = list(tpl)
#     if elem in tpl:
#         lst.remove(elem)
#     return tuple(lst)
# print(del_from_tuple((1, 2, 3), 1))
# print(del_from_tuple((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
# print(del_from_tuple((2, 4, 6, 6, 4, 2), 9))

#
# PROBLEM 11
#
# Создать Лист и заполнить его 5 РАЗНЫМИ ТИПАМИ ДАННЫХ.

# a = [20, 3, 2007]
# b = ['name esen']
# c = ['surname azamtov']
# r = [16, 9, 'september']
# q = [550560321]
# print(a, b, c, r, q)

# PROBLEM 0
#
# 1.Создать Лист из 5 разных имён.
#
# 2.Создать пустую строку и через .join() соеденить пустую строку и все имена в списке.
# p = ""
# t = ['Esen', 'Artur', 'Aidar', 'Azamat', 'Kayrat']
# print(p.join(t))

# PROBLEM 12
#
# Создать Tuple из 15 различных объектов.

# Разрезать Tuple
# на 5 строк по 3 объекта в строке.
# a = ("hello", 'peaple', 'who', 'are', 'you', 'esen', 'esene', 'azamat', 'name', '20', '30', '2020', '1', '2121', '35')
# print(a[0:3], a[3:6], a[6:9], a[9:12], a[12:15])

# PROBLEM 17
#
# Взять Лист №1 и посчитать сколько раз там встречается имя "Jack".

# ЛИСТ №1:

# NAMES = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON',  'JIMMY', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',].count("JACK")
# print(NAMES)

# PROBLEM 72
#
# Удалить из Листа №1 все чётные индексы до 10.
#
# names = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON',  'JIMMY', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',]
# names.pop(0)
# names.pop(2)
# names.pop(4)
# names.pop(6)
# names.pop(8)
# names.pop(10)
# print(names)

# PROBLEM 1
#
# Создать пустой лист.
#
# Добавить в него сначала Ваше Имя, Год Рождения, любимый Язык Программирования.

# d = []
# d.append('esen')
# d.append("2007")
# d.append("my faivorite languege Python")
# print(d)