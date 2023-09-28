#!/usr/bin/python3

def uniq_add(my_list=[]):
    lista_uniq = set(my_list)
    suma = 0
    for i in lista_uniq:
        suma += i
    return (suma)
