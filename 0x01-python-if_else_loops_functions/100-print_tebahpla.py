#!/usr/bin/python3

def toggle(case):
    if case is True:
        return False
    if case is False:
        return True


lowercase = True
for i in range(122, 96, -1):
    if lowercase is False:
        i = i - 32
    print("{}".format(chr(i)), end="")
    lowercase = toggle(lowercase)
