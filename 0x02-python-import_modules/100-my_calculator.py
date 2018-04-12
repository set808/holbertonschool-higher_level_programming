#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def is_operator(operator):
    operators = ['+', '-', '*', '/']
    for i in operators:
        if operator == i:
            return True
    return False


def calc(argv):
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if is_operator(operator) is False:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    if operator == '+':
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif operator == '-':
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    elif operator == '*':
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    elif operator == '/':
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))

if __name__ == '__main__':
    import sys
    calc(sys.argv)
