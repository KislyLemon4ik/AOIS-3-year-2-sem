from spreadsheet import *
from bin_dec import *


def SKNF(formula):
    formula_sknf = ''
    dat_table = create_logic_table(formula)[1]
    for n in dat_table:
        if n['f'] == 0:
            part = ' + '.join([values * '!' + keys for keys, values in n.items() if keys != 'f' and keys != 'n'])

            formula_sknf += '( ' + str(part) + ' )' + ' * '
    formula_sknf = formula_sknf[:-2]
    return formula_sknf

def fraction_to_binary(fraction, places):
    binary_digits = []
    count = 1
    while count <= places:
        fraction *= 2

        digit = int(fraction)
        fraction -= digit

        binary_digits.append(digit)
        count += 1
    return binary_digits

def SKNF_form_number(form):
    split_SKNF = SKNF(form).split()
    SKNF_bin = ''.join(['0' if s[0] == 'x' else '1' if s[0] == '!' else '*' for s in split_SKNF])
    SKNF_dec = '*(' + ', '.join(map(str, bin_dec(SKNF_bin, form))) + ')'
    return SKNF_bin, SKNF_dec

def calculate_sknf(formula):
    sknf_formula = ''
    data_table = create_logic_table(formula)[1]
    for row in data_table:
        if row['f'] == 0:
            part = ' + '.join([bin_dec.negate_value(values) + keys for keys, values in row.items() if keys != 'f' and keys != 'n'])
            sknf_formula += '( ' + str(part) + ' )' + ' * '
    sknf_formula = sknf_formula[:-2]
    return sknf_formula

def fraction_to_binary(fraction, places):
    binary_digits = []
    count = 1
    while count <= places:
        fraction *= 2
        digit = int(fraction)
        binary_digits.append(digit)
        fraction -= digit
        count += 1
    return binary_digits

def calculate_sknf_number(formula):
    sknf_formula = calculate_sknf(formula)
    split_sknf = sknf_formula.split()
    sknf_binary = ''.join(['0' if s[0] == 'x' else '1' if s[0] == '!' else '*' for s in split_sknf])
    sknf_decimal = '*(' + ', '.join(map(str, bin_dec.binary_to_decimal(sknf_binary, formula))) + ')'
    return sknf_binary, sknf_decimal


