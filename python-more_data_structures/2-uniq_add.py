#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    lista_uniq = set(my_list)
    suma = 0
    for i in lista_uniq:
        suma += i
    return (suma)
