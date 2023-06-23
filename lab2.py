indexs = {
    'x1': [0, 0, 0, 0, 1, 1, 1, 1],
    'x2': [0, 0, 1, 1, 0, 0, 1, 1],
    'x3': [0, 1, 0, 1, 0, 1, 0, 1]
}

ind_numbers = 3


# (x1+x2)*!x3

def to_pdnf(ix, result, talbe):
    if talbe[ix] == 1:
        if result != '':
            result = result + '+'
        result = result + '('
        arg_index = 1
        for x in indexs.values():
            if x[ix] == 0:
                result = result + '!'
            result = result + 'x' + str(arg_index)
            arg_index += 1
            if arg_index <= ind_numbers:
                result = result + '*'
        result = result + ')'
    return result


def num_pdnf(talbe):
    num = []
    for ix in range(len(talbe)):
        pdnf_numm(ix, num, talbe)
    num_form = ','.join(num)
    num_form = '\\/(' + num_form + ')'
    return num_form


def pdnf_numm(ix, num, talbe):
    if talbe[ix] == 1:
        num.append(0)
        if indexs['x1'][ix] == 1:
            num[-1] += 4
        if indexs['x2'][ix] == 1:
            num[-1] += 2
        if indexs['x3'][ix] == 1:
            num[-1] += 1
        num[-1] = str(num[-1])

def solution(argument1, argument2, oper):
    if oper == '->':
        result = [implicaton(argument1, argument2)]
    if oper == '~':
        result = [ecvivalence(argument1, argument2)]
    if oper == '+':
        result = [disconnection(argument1, argument2)]
    if oper == '*':
        result = [connection(argument1, argument2)]
    return result

def find_matching_bracket_index(lines):
    br = 1
    ix = 0
    ix = find_matching_bracket_index_while(br, ix, lines)
    return ix



def tru_talbe_while(arguments, ix, lines):
    while ix < len(lines):
        if lines[ix] == '(':
            start = ix + 1
            ix = ix + find_matching_bracket_index(lines[start:])
            arguments.append(tru_talbe(lines[start:ix]))
        elif lines[ix] == 'x':
            arguments.append(indexs[lines[ix:ix + 2]])
            ix += 1
        elif lines[ix] == '!':
            if lines[ix + 1] == 'x':
                arguments.append(invert_bits(indexs[lines[ix + 1:ix + 3]]))
                ix += 2
            elif lines[ix + 1] == '(':
                start = ix + 2
                ix = ix + find_matching_bracket_index(lines[start:]) + 1
                arguments.append(invert_bits(tru_talbe(lines[start:ix])))
        else:
            oper = lines[ix]
            if oper == '-':
                ix += 1
                oper = oper + lines[ix]
        if len(arguments) == 2:
            arguments = solution(arguments[0], arguments[1], oper)
        ix += 1
    return arguments

def connection(x, y):
    result = [0 for ix in range(8)]
    connection_for(result, x, y)
    return result

def find_matching_bracket_index_while(br, ix, lines):
    while br > 0:
        if lines[ix] == '(':
            br += 1
        elif lines[ix] == ')':
            br -= 1
        ix += 1
    return ix


def disconnection(x, y):
    result = [1 for ix in range(8)]
    disconnection_for(result, x, y)
    return result


def ecvivalence_for(result, x, y):
    for ix in range(8):
        if x[ix] == y[ix]:
            result[ix] = 1

def implicaton(x, y):
    result = [1 for ix in range(8)]
    implicaton_for(result, x, y)
    return result



def ecvivalence(x, y):
    result = [0 for ix in range(8)]
    ecvivalence_for(result, x, y)
    return result

def invert_bits(bit_list):
    return [1 if bits == 0 else 0 for bits in bit_list]



def connection_for(result, x, y):
    for ix in range(8):
        if x[ix] == 1 and y[ix] == 1:
            result[ix] = 1

def tru_talbe(lines):
    ix = 0
    arguments = []
    arguments = tru_talbe_while(arguments, ix, lines)
    return arguments[0]

def to_decl(number_bin):
    ix = 0
    number_dec = 0
    number_dec = to_decl_for(ix, number_bin, number_dec)
    return number_dec

def implicaton_for(result, x, y):
    for ix in range(8):
        if x[ix] == 1 and y[ix] == 0:
            result[ix] = 0

def disconnection_for(result, x, y):
    for ix in range(8):
        if x[ix] == 0 and y[ix] == 0:
            result[ix] = 0

def pcnf(talbe):
    result = ''
    result = to_pcnf(result, talbe)
    return result


def to_pcnf(result, talbe):
    for ix in range(len(talbe)):
        if talbe[ix] == 0:
            if result != '':
                result = result + '*'
            result = result + '('
            arg_index = 1
            for x in indexs.values():
                if x[ix] == 1:
                    result = result + '!'
                result = result + 'x' + str(arg_index)
                arg_index += 1
                if arg_index <= ind_numbers:
                    result = result + '+'
            result = result + ')'
    return result


def num_pcnf(talbe):
    num = []
    for ix in range(len(talbe)):
        pcnf_numm(ix, num, talbe)
    num_form = ','.join(num)
    num_form = '/\\(' + num_form + ')'
    return num_form

def to_decl_for(ix, number_bin, number_dec):
    while ix < len(number_bin):
        number_dec = number_dec + (2 ** (len(number_bin) - ix - 1)) * number_bin[ix]
        ix += 1
    return number_dec

def pdnf(talbe):
    result = ''
    for ix in range(len(talbe)):
        result = to_pdnf(ix, result, talbe)
    return result

def pcnf_numm(ix, num, talbe):
    if talbe[ix] == 0:
        num.append(0)
        if indexs['x1'][ix] == 1:
            num[-1] += 4
        if indexs['x2'][ix] == 1:
            num[-1] += 2
        if indexs['x3'][ix] == 1:
            num[-1] += 1
        num[-1] = str(num[-1])

lines = input("Ваше выраажение: ")
result = tru_talbe(lines)

print('\nТаблица истинности:')
print('x1->  ' + '  '.join(str(elelement) for elelement in indexs['x1']))

print('x2->  ' + '  '.join(str(elelement) for elelement in indexs['x2']))

print('x3->  ' + '  '.join(str(elelement) for elelement in indexs['x3']))

print('f->   ' + '  '.join(str(elelement) for elelement in result))

print('\nИндексная ф-ма: ' +  str(to_decl(result)))
print('Числовая ф-ма: ' + num_pcnf(result) + ' = ' + num_pdnf(result))

print('\nскнф: ' + pcnf(result))
print('сднф: ' + pdnf(result) + '\n')
