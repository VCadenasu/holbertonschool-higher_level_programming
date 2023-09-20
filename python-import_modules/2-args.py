#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    i = 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("{} argument:".format(argc))
    else:
        print("{} arguments:".format(argc))
while i <= argc:
    print("{}: {}".format(i, sys.argv[i]))
    i += 1
