#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed += 1
    except IndexError:
        pass
    print()  # To print a new line at the end
    return printed
