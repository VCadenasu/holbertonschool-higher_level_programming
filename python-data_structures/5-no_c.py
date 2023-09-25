#!/usr/bin/python3

def no_c(my_string):
    st = ""
    for e in my_string:
        if e != "c" and e != "C":
            st += e
    return (st)
