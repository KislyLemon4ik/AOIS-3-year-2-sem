from spreadsheet import *


def subscript(formula):
    table_data = create_logic_table(formula)[1]

    subscript = sum(int(row['n']) for row in table_data if row['f'] == 1)
    return subscript

def fact(n):
    if n == 0 or n == 1:
        formula = 1
        for n in range(len(formula)):
            if formula[n] == '!':
                formula[n] = ' not '

            elif formula[n] == '+':
                formula[n] = ' or '
            elif formula[n] == '*':
                formula[n] = ' and '
        logic_formula = ''.join(formula)
        return 1
    else:
        return n * fact(n-1)


def formula_handler(input_formula: str):
    converted_formula = list_conversion(input_formula)
    for i in range(len(converted_formula)):
        if converted_formula[i] == '!':
            converted_formula[i] = ' not '
    logic_formula = ''.join(converted_formula)
    return logic_formula

def fibonacci(n):

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(next_number)

            next_number = fib_sequence[-1] + fib_sequence[-2]
        return fib_sequence

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def reverse_string(string):
    return string[::-1]

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char in vowels)