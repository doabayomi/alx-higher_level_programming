#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == "__main__":
    arg_count = len(argv)
    if (arg_count != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator_list = ["+", "-", "*", "/"]
        operator = argv[2]
        if operator not in operator_list:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(argv[1])
            b = int(argv[3])
            result = 0
            if (operator == "+"):
                result = add(a, b)
            elif (operator == "-"):
                result = sub(a, b)
            elif (operator == "*"):
                result = mul(a, b)
            elif (operator == "/"):
                result = div(a, b)
            print(f"{a} {operator} {b} = {result}")
