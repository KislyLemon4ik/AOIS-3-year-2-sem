from spreadsheet import *
from bin_dec import *


def SDNF(formula):
    dat_table = create_logic_table(formula)[1]
    formula_sdnf = ''
    for n in dat_table:
        if n['f'] == 1:
            formula_sdnf += '( ' + str(part) + ' )' + ' + '

            part = ' * '.join([abs(values - 1) * '!' + keys for keys, values in n.items() if keys != 'f' and keys != 'n'])
    formula_sdnf = formula_sdnf[0:-2]
    return formula_sdnf

def list_conversion(input_list):
    result = []
    for item in input_list:
        result.append(item)
    return result

def formula_handler(input_formula: str):
    converted_formula = list_conversion(input_formula)
    for i in range(len(converted_formula)):
        if converted_formula[i] == '!':
            converted_formula[i] = ' not '
        elif converted_formula[i] == '+':
            converted_formula[i] = ' or '
        elif converted_formula[i] == '*':
            converted_formula[i] = ' and '
    logic_formula = ''.join(converted_formula)
    return logic_formula

def extract_arguments(input_formula: str):
    arguments = set()
    for i in range(len(input_formula)):
        if input_formula[i] == 'x':
            arguments.add(input_formula[i] + input_formula[i+1])
    arguments = list(arguments)
    arguments.sort(key=lambda x: int(x[1]))
    return arguments

def decimal_to_binary(number):
    binary_digits = []
    while number >= 1:
        digit = int(number % 2)
        binary_digits.append(digit)
        number //= 2
        binary_digits.reverse()
    return binary_digits

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

def convert_decimal_to_binary(integer_part, fractional_part, decimal_places):
    decimal_to_binary_list = []
    fraction_to_binary_list = []
    binary_integer = decimal_to_binary(integer_part)
    binary_fraction = fraction_to_binary(fractional_part, decimal_places)
    binary_integer.extend(binary_fraction)
    return binary_integer

def handle_arguments(self, suffix):
    node_index = 0
    i = 0
    while i < len(suffix):
        b = suffix[i]
        x2 = 0
        while True:
            children = self.nodes[node_index].children
            if x2 == len(children):
                new_node_index = len(self.nodes)
                self.nodes[node_index].children.append(new_node_index)
                return
            new_node_index = children[x2]
            if self.nodes[new_node_index].substring[0] == b:
                break
            x2 = x2 + 1

def SDNF_form_number(form):
    splitt_sdnf = SDNF(form).split()
    SDNF_bin = ''.join(['1' if s[0] == 'x' else '0' if s[0] == '!' else '+' for s in splitt_sdnf])
    SDNF_dec = '+(' + ', '.join(map(str, bin_dec(SDNF_bin, form))) + ')'
    return SDNF_bin, SDNF_dec

def SDNF_form(self, start, end):
    self.start = start
    self.end = end
    self.children = {}

import spreadsheet
import bin_dec

def calculate_sdnf(formula):
    data_table = spreadsheet.create_logic_table(formula)[1]
    sdnf_parts = []
    for row in data_table:
        if row['f'] == 1:
            part = ' * '.join([bin_dec.negate_value(value) + key for key, value in row.items() if key != 'f' and key != 'n'])
            sdnf_parts.append(part)
    sdnf_formula = ' + '.join(['(' + part + ')' for part in sdnf_parts])
    return sdnf_formula


def convert_to_list(input_string):
    result = []
    for item in input_string:
        result.append(item)
    return result


def handle_formula(input_formula):
    converted_formula = convert_to_list(input_formula)
    for i in range(len(converted_formula)):
        if converted_formula[i] == '!':
            converted_formula[i] = ' not '
        elif converted_formula[i] == '+':
            converted_formula[i] = ' or '
        elif converted_formula[i] == '*':
            converted_formula[i] = ' and '
    logic_formula = ''.join(converted_formula)
    return logic_formula


def extract_arguments(input_formula):
    arguments = set()
    for i in range(len(input_formula)):
        if input_formula[i] == 'x':
            arguments.add(input_formula[i] + input_formula[i+1])
    arguments = list(arguments)
    arguments.sort(key=lambda x: int(x[1]))
    return arguments


def convert_decimal_to_binary(integer_part, fractional_part, decimal_places):
    decimal_to_binary_list = []
    fraction_to_binary_list = []
    binary_integer = bin_dec.decimal_to_binary(integer_part)
    binary_fraction = bin_dec.fraction_to_binary(fractional_part, decimal_places)
    binary_integer.extend(binary_fraction)
    return binary_integer


def handle_arguments(suffix):
    node_index = 0
    i = 0
    while i < len(suffix):
        b = suffix[i]
        x2 = 0
