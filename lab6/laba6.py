length_of_table = 20
length_of_alphabet = 26
index_of_key = 1
index_v = 2
index_h = 3
index_of_info = 4
index_of_collision = 5

def row_printer(rows):
    outpt = "{0:^3}|{1:^14}|{2:^5}|{3:^6}|{4:^5}| {5}".format(
        rows[0], rows[index_of_key], rows[index_v], rows[index_h], rows[index_of_collision], rows[index_of_info]
    )
    print(outpt)


def table_printer(tabe):
    toper = " № |     term     |  V  | h(V) |  C  | definition"
    spr = "---+--------------+-----+------+-----+-------------------------------------------------------------------"

    print('\n'.join([toper, spr]))
    for rows in tabe:
        row_printer(rows)
    print(spr)


def value_calculate(keys):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    first_l = alph.index(keys[0])
    second_l = alph.index(keys[1])
    val = first_l * len(alph) + second_l
    return val


def address_calculate(val):
    addr = val % length_of_table
    return addr

def empty_find(tabe):
    for ix, rows in enumerate(tabe):
        if rows[index_of_key] == '':
            return ix
        
def last_find(tabe, addr):
    if tabe[addr][index_of_collision] == '':
        return addr
    return last_find(tabe, tabe[addr][index_of_collision])

        
def to_add(tabe, keys, information):
    val = value_calculate(keys)
    addr = address_calculate(val)
    addition(addr, information, keys, tabe, val)


def addition(addr, information, keys, tabe, val):
    if tabe[addr][index_of_key] == '':
        tabe[addr] = [addr, keys, val, addr, information, '']
    elif tabe[addr][index_h] != addr:
        keys_other = tabe[addr][index_of_key]
        information_other = tabe[addr][index_of_key]
        row_delete(keys_other, tabe)
        tabe[addr] = [addr, keys, val, addr, information, '']
        to_add(tabe, keys_other, information_other)
    else:
        index = empty_find(tabe)
        last = last_find(tabe, addr)
        tabe[last][index_of_collision] = index
        tabe[index] = [index, keys, val, addr, information, '']


def row_finder(keys, tabe, addr=None):
    if addr is None:
        val = value_calculate(keys)
        addr = address_calculate(val)

    return row_finder_while(addr, keys, tabe)


def row_finder_while(addr, keys, tabe):
    while addr != '':
        if tabe[addr][index_of_key] == keys:
            return tabe[addr]
        addr = tabe[addr][index_of_collision]
    return None


def previous_find(tabe, addr):
    for ix, row in enumerate(tabe):
        if row[index_of_collision] == addr:
            return ix

            
def row_delete(keys, tabe, addr=''):
    if addr == '':
        val = value_calculate(keys)
        addr = address_calculate(val)
    if tabe[addr][index_of_key] == keys:
        row_deleter(addr, tabe)
    else:
        row_delete(keys, tabe, addr=tabe[addr][index_of_collision])


def row_deleter(addr, tabe):
    if tabe[addr][index_of_collision] == '' and addr == tabe[addr][index_h]:
        tabe[addr] = [addr, '', '', '', '', '']
    elif tabe[addr][index_of_collision] != '':
        index_next = tabe[addr][index_of_collision]
        tabe[addr] = tabe[index_next]
        tabe[addr][0] = addr
        tabe[index_next] = [index_next, '', '', '', '', '']
    else:
        previously_index = previous_find(tabe, addr)
        tabe[previously_index][index_of_collision] = tabe[addr][index_of_collision]
        tabe[addr] = [addr, '', '', '', '', '']


tabe = []
for ix in range(length_of_table):
    tabe.append([ix, '', '', '', '', ''])
information = open('ph.txt')
lines = information.readlines()
collisions = []
for line in lines:
    keys, information = line.split(', ')
    information = information.replace('\n', '')
    val = value_calculate(keys)
    addr = address_calculate(val)
    rows = [addr, keys, val, addr, information, '']
    if tabe[addr][index_of_key] == '':
        tabe[addr] = rows
    else:
        collisions.append(rows)
for rows in collisions:
    to_add(tabe, rows[index_of_key], rows[index_of_info])
table_printer(tabe)

while True:
    opt = input('\n1 - show the table\n2 - add new term\n3 - find a term\n4 - delete a term\n')
    match opt:
        case '1':
            table_printer(tabe)
        case '2':
            keys = input('\nterm: ')
            if row_finder(keys, tabe) is not None:
                print('This term already exists.')
            else:
                information = input('definition: ')
                to_add(tabe, keys, information)
        case '3':
            keys = input('\nterm: ')
            term = row_finder(keys, tabe)
            if term is None:
                print('Term not found.')
            else:
                table_printer([term])
        case '4':
            keys = input('\nterm: ')
            row_delete(keys, tabe)


