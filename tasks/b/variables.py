"""
Создайте три переменные с именами int_var, float_var и str_var.
Присвойте им значения 4, корень из 67 и '#just_a_hashtag', соответственно.

Какие пары из этих значений можно умножать друг на друга?
Создайте еще четыре переменные p1, p2, p3 и p4 с различными значениями их произведений.
    > можно умножать переменную на саму себя
    > int_var * float_var и float_var * int_var - это одно и то же произведение

Запустите файл (Right Click -> Run или Ctrl + Shift + F10),
убедитесь, что выводятся четыре различных значения.
"""

int_var = 4
float_var = 67 ** 0.5
str_var = '#just_a_hashtag'

p1 = int_var * int_var
p2 = float_var * float_var
p3 = int_var * float_var
p4 = int_var * str_var

print(p1, p2, p3, p4, sep='\n')
