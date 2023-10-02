#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    orden = list(a_dictionary)
    orden.sort()
    for n in orden:
        print("{}: {}".format(n, a_dictionary.get(n)))
