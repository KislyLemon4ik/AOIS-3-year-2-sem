from prettytable import PrettyTable
from itertools import product
from typing import *
from handler_input import *


def replace_argument_on_number(set_of_values, argu, temp_logical):
    counter = 0
    for n in argu:
        temp_logical = temp_logical.replace(n, str(set_of_values[counter]))
        counter += 1
    return temp_logical

def list_conversion(input_list):
    result = []
    for item in input_list:
        result.append(item)
    return result

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

        substring2 = self.nodes[new_node_index].substring
        j = 0
        while j < len(substring2):
            if suffix[i + j] != substring2[j]:
                node_index2 = new_node_index
                new_node_index = len(self.nodes)
                self.nodes[node_index2].substring = substring2[j:]
                self.nodes[node_index].children[x2] = new_node_index
                break
            j = j + 1
        i = i + j
        node_index = new_node_index

def decimal_to_binary(convert):
    binary_integer=[]
    while(convert/2>=1):
        i=int(convert%2)
        binary_integer.append(i)
        convert/=2
    if(len(binary_integer)>1):
        binary_integer.reverse()
    binary_integer.insert(0,1)
    return binary_integer


def decimail(number):
    number_str = str(number).replace('-', '')
    decimal_part = number_str.split('.')[0]
    fraction_part = number_str.split('.')[1]

    signal_bit = (1 if number < 0 else 0)

    decimal_bits = ''
    fraction_bits = ''

    mantissa_available_bits = 23

    if decimal_part:
        decimal_part = int(decimal_part)

    if fraction_part:
        fraction_part = float('0.' + fraction_part)
        extra_bits = 0
        count_zeros_to_the_left = True

        while len(fraction_bits) < (mantissa_available_bits + extra_bits):
            product = fraction_part * 2

            bit = '1' if product >= 1 else '0'

            fraction_bits += bit

            fraction_part = str(product).split('.')[1]

            if fraction_part == '0':
                fraction_part = 0
                break

            fraction_part = float('0.' + fraction_part)

            if count_zeros_to_the_left:
                extra_bits = 0
                for fraction_bit in fraction_bits:
                    if fraction_bit == '0':
                        extra_bits += 1
                    else:
                        count_zeros_to_the_left = False
                        break

        if not fraction_bits:
            fraction_bits = '0'

        # round binary
        if fraction_part != 0:
            fraction_bits += '1'

    mantissa = decimal_bits + fraction_bits
    exponent = 0
    zeros_shifted = mantissa.find('1')

    exponent = len(decimal_bits) - 1

    if decimal_bits == '0':
        exponent -= 1

    if zeros_shifted > 0:
        exponent -= zeros_shifted - 1

    mantissa = mantissa[zeros_shifted + 1:mantissa_available_bits].ljust(mantissa_available_bits, '0')

    exponent += 127


    return f'{signal_bit}{mantissa}'


def create_logic_table(formula):
    argu = take_arguments(formula)
    logic_formula = handler_input_formula(formula)
    table_data = list()
    table = PrettyTable()
    table.field_names = [*argu, 'f(SKNF)', 'f(SDNF)', 'n']
    value_arguments: List[Tuple[int]] = product(range(2), repeat=len(argu))
    starter_index = 2 ** (2 ** len(argu) - 1)


    for n in value_arguments:
        temp_logical = logic_formula
        temp_logical = replace_argument_on_number(n, argu, temp_logical)
        table.add_row([*n, int(eval(temp_logical)), int(eval(temp_logical)), starter_index])
        data_for_row = {argu[x]: n[x] for x in range(len(argu))}
        data_for_row = {**data_for_row, 'f': int(eval(temp_logical)), 'n': starter_index}
        table_data.append(data_for_row)
        starter_index //= 2

    return table, table_data
