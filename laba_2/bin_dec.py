from handler_input import *


def bin_dec(form, formula):
    argu = take_arguments(formula)
    rez = [0]
    subscript = 0

    binar_power = len(argu) - 1
    for n in form:
        if n == '*' or n == '+':
            binar_power = len(argu) - 1
            rez.append(0)
            subscript += 1
            continue
        rez[subscript] += int(n) * (2**binar_power)
        binar_power -= 1
    return rez

def extract_arguments(input_formula: str):
    arguments = set()
    for i in range(len(input_formula)):
        if input_formula[i] == 'x':
            arguments.add(input_formula[i] + input_formula[i+1])
    arguments = list(arguments)
    arguments.sort(key=lambda x: int(x[1]))
    return arguments

def bin(int_number, available_places):
    bits = ''

    while int_number > 0 and len(bits) < available_places:
        quotient = int_number / 2;
        has_decimal = quotient % 1 != 0

        if has_decimal:
            bits = '1' + bits
        else:
            bits = '0' + bits

        int_number = int(quotient)

    if not bits:
        bits = '0'

    return bits

def list_to_string(list):
    list_string=''.join([str(elem) for elem in list ])
    return list_string