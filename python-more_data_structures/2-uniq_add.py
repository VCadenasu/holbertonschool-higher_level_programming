#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    lista_uniq = set(my_list)
    suma = reduce(lambda a, b: a + b, lista_uniq)
    return (suma)
