from operator import ifloordiv


def add(num1, num2):
    return num1 + num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

def neliosumma(lista_a):
    summa = 0
    for i in lista_a:
        summa += i ** 2
    print(summa)
    return summa

def is_min_length(s):
    if  len(s) < 8:
        return False
    return True

def non_negative(luvut):    
    non_negative_list = [x for x in luvut if x >= 0]
    return non_negative_list

        