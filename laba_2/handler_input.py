def convert_for_list(formula):
    rez = []
    for n in formula:
        rez.append(n)
    return rez

def handler_input_formula(formula: str):
    formula = convert_for_list(formula)
    for n in range(len(formula)):
        if formula[n] == '!':
            formula[n] = ' not '
        elif formula[n] == '+':
            formula[n] = ' or '
        elif formula[n] == '*':
            formula[n] = ' and '
    logic_formula = ''.join(formula)
    return logic_formula


def take_arguments(formula: str):
    argu = set()
    for n in range(len(formula)):
        if formula[n] == 'x':
            argu.add(formula[n] + formula[n+1])
    argu = list(argu)
    argu.sort(key=lambda x: int(x[1]))
    return argu

def decimal__binary(number):
    binary_digits = []
    while number >= 1:
        digit = int(number % 2)
        binary_digits.append(digit)
        number //= 2
        binary_digits.reverse()
    return binary_digits

def fraction_binary(fraction, places):
    binary_digits = []
    count = 1
    while count <= places:
        fraction *= 2
        digit = int(fraction)
        binary_digits.append(digit)
        fraction -= digit
        count += 1
    return binary_digits

def convert_decimal_binary(integer_part, fractional_part, decimal_places):
    decimal_to_binary = []
    fraction_to_binary = []
    binary_integer = decimal_to_binary(integer_part)
    binary_fraction = fraction_to_binary(fractional_part, decimal_places)
    binary_integer.extend(binary_fraction)
    return binary_integer

def arguments(self, suf):
    n = 0
    i = 0
    while i < len(suf):
        b = suf[i]
        x2 = 0
        while True:
            children = self.nodes[n].ch
            if x2 == len(children):
                n2 = len(self.nodes)
                self.nodes[n].ch.append(n2)
                return
            n2 = children[x2]
            if self.nodes[n2].sub[0] == b:
                break
            x2 = x2 + 1

        sub2 = self.nodes[n2].sub
        j = 0
        while j < len(sub2):
            if suf[i + j] != sub2[j]:
                n3 = n2
                n2 = len(self.nodes)
                self.nodes[n3].sub = sub2[j:]
                self.nodes[n].ch[x2] = n2
                break
            j = j + 1
        i = i + j
        n = n2

def convert_formula_to_list(formula):
    result = []
    for char in formula:
        result.append(char)
    return result

def handle_input_formula(formula):
    formula_list = convert_formula_to_list(formula)
    for i in range(len(formula_list)):
        if formula_list[i] == '!':
            formula_list[i] = ' not '
        elif formula_list[i] == '+':
            formula_list[i] = ' or '
        elif formula_list[i] == '*':
            formula_list[i] = ' and '
    logic_formula = ''.join(formula_list)
    return logic_formula

def extract_arguments(formula):
    arguments = set()
    for i in range(len(formula)):
        if formula[i] == 'x':
            arguments.add(formula[i] + formula[i+1])
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

def convert_decimal_binary(integer_part, fractional_part, decimal_places):
    binary_integer = decimal_to_binary(integer_part)
    binary_fraction = fraction_to_binary(fractional_part, decimal_places)
    binary_integer.extend(binary_fraction)
    return binary_integer

def handle_arguments(self, suffix):
    node_index = 0
    i = 0
    while i < len(suffix):
        b = suffix[i]
        child_index = 0
        while True:
            children = self.nodes[node_index].children
            if child_index == len(children):
                new_node_index = len(self.nodes)
                self.nodes[node_index].children.append(new_node_index)
                return
            new_node_index = children[child_index]
            if self.nodes[new_node_index].substring[0] == b:
                break
            child_index += 1

        sub2 = self.nodes[new_node_index].substring
        j = 0
        while j < len(sub2):
            if suffix[i + j] != sub2[j]:
                prev_node_index = new_node_index
                new_node_index = len(self.nodes)
                self.nodes[prev_node_index].substring = sub2[j:]
                self.nodes[node_index].children[child_index] = new_node_index
                break
            j += 1
        i += j
        node_index = new_node_index

