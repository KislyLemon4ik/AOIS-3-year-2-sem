import laba2 as pp

height_of_table = 2
width_of_table = 4
number_of_arguments = 3


def types(lines):
    types_list = []
    ix = 0
    while ix < len(lines):
        if lines[ix] == '+':
            types_list.append('con')
        elif lines[ix] == '*':
            types_list.append('dis')
        ix += 1
    return types_list




def x_find(finder, index, ix, miss, talbes):
    if ix != miss:
        if talbes[ix][index] == 'x':
            finder = True
    return finder


def to_quin(talbes, impls):
    ix = 0
    to_reduce = impls.copy()
    table2 = talbes.copy()
    to_quien(ix, table2, to_reduce)
    return to_reduce


def reading_line(lines):
    perfectly_form = []
    ix = 0
    read_of_lines(ix, lines, perfectly_form)
    return perfectly_form


def read_of_lines(ix, lines, perfectly_form):
    while ix < len(lines):
        if lines[ix] == '(':
            perfectly_form.append(brackets_reading(lines[ix:]))
        ix += 1


def mergebles(const1, const2, argument_index):
    mergeability = True
    mergeability = mergebles2(argument_index, const1, const2, mergeability)
    return mergeability




def merg2(formula):
    was_merged = []
    was_used = [False for ix in range(len(formula))]
    merge4(formula, was_merged, was_used)
    for ix in range(len(was_used)):
        if not(was_used[ix]):
            was_merged.append(formula[ix])
    return was_merged

def merg3(formula, was_merged, was_used):
    for ix in range(number_of_arguments):
        for jx in range(len(formula) - 1):
            for k in range(jx + 1, len(formula)):
                if mergebles(formula[jx], formula[k], ix):
                    was_used[jx] = True
                    was_used[k] = True
                    was_merged.append(formula[jx].copy())
                    was_merged[-1].pop(ix)
                    was_merged[-1].insert(ix, -1)
                    break


def merge4(formula, was_merged, was_used):
    for ix in range(number_of_arguments):
        for jx in range(len(formula) - 1):
            for k in range(jx + 1, len(formula)):
                if mergebles(formula[jx], formula[k], ix):
                    was_used[jx] = True
                    was_used[k] = True
                    was_merged.append(formula[jx].copy())
                    was_merged[-1].pop(ix)
                    was_merged[-1].insert(ix, -1)
                    break


def sub(formula, val):
    for ix in range(len(val)):
        if val[ix] == -1:
            value_misserd = ix
    for ix in range(len(formula)):
        if formula[ix] != -1 and ix != value_misserd:
            argument_existing = ix
    result = []
    result.append(formula[value_misserd])
    return argument_existing, result


def delte_exc(formtype, ix, new_formulas, no_ch):
    while ix < len(new_formulas):
        result = []
        for oth in new_formulas:
            if new_formulas[ix] != oth:
                sub = replacement(new_formulas[ix], oth, formtype)
                if sub[1] == no_ch:
                    result.append(sub[0])
        poss = False
        negat = False
        for args in result:
            if args == 0:
                negat = True
            if args == 1:
                poss = True
        if poss and not negat:
            new_formulas.pop(ix)
        else:
            ix += 1



def excession_delete(formula, formtype):
    new_formulas = formula.copy()
    if formtype == 'dis':
        no_ch = 1
    else:
        no_ch = 0
    ix = 0
    delte_exc(formtype, ix, new_formulas, no_ch)
    return new_formulas

def mergebles2(argument_index, const1, const2, mergeability):
    for ix in range(len(const1)):
        if ix != argument_index and const1[ix] != const2[ix]:
            mergeability = False
            break
        if ix == argument_index and const1[ix] == const2[ix]:
            mergeability = False
            break
    return mergeability

def merg(formula):
    was_merged = []
    was_used = [False for ix in range(len(formula))]
    merg3(formula, was_merged, was_used)
    for el in was_used:
        if not(el):
            return None
    return was_merged



def find_impl(duos, tabl):
    for ix in range(height_of_table):
        for jx in range(width_of_table):
            if tabl[ix][jx] == 1 and tabl[ix][to_next(jx, width_of_table)] == 1:
                duos.append([numbers(ix, jx), numbers(ix, to_next(jx, width_of_table))])
    for jx in range(width_of_table):
        if tabl[0][jx] == 1 and tabl[1][jx] == 1:
            duos.append([numbers(0, jx), numbers(1, jx)])
    ix = 0
    while ix < len(duos):
        if is_excess(duos[ix], duos):
            duos.pop(ix)
        else:
            ix += 1



def pair_to_implicant(pair, formtype):
    formula = []
    zero_range = 3
    for ix in range(len(pair)):
        if pair[ix] > zero_range:
            x1 = 1
            pair[ix]-=width_of_table
        else:
            x1 = 0
        if pair[ix] == 0:
            x2, x3 = 0, 0
        if pair[ix] == 1:
            x2, x3 = 0, 1
        if pair[ix] == 2:
            x2, x3 = 1, 1
        if pair[ix] == 3:
            x2, x3 = 1, 0
        formula.append([x1,x2,x3])
    implicant = merg(formula)[0]
    if formtype == 'con':
        implicant = reverse_method(implicant)
    return implicant

def implicants(tabl, formtype):
    duos = []
    find_impl(duos, tabl)
    impls = []
    for pair in duos:
        impls.append(pair_to_implicant(pair, formtype))
    return impls



def is_excess(pair, duos):
    first_find = False
    second_find = False
    for oth in duos:
        if oth != pair:
            if oth[1] == pair[0] or oth[0] == pair[0]:
                first_find = True
            if oth[0] == pair[1] or oth[1] == pair[1]:
                second_find = True
    return first_find and second_find


def x_finder(talbes, miss, index):
    finder = False
    for ix in range(len(talbes)):
        finder = x_find(finder, index, ix, miss, talbes)
    return finder



def numbers(ix, jx):
    return ix << 2 | jx


def brackets_reading(lines):
    ix = 0
    const = []
    reading_of_brackets(const, ix, lines)
    return const


def reading_of_brackets(const, ix, lines):
    while lines[ix] != ')':
        if lines[ix] == 'x':
            if lines[ix - 1] == '!':
                const.append(0)
            else:
                const.append(1)
        ix += 1


def str_form_fro(formula, ins, length_of_argu, substr):
    for ix in range(len(formula)):
        args = []
        for jx in range(len(formula[ix])):
            if formula[ix][jx] == 0:
                args.append('!x' + str(jx + 1))
            if formula[ix][jx] == 1:
                args.append('x' + str(jx + 1))
        substr.append(ins.join(args))
        if len(substr[-1]) > length_of_argu:
            substr[-1] = '(' + substr[-1] + ')'


def method_of_metod(formtype, formula, tabl):
    for constit in formula:
        if formtype == 'con':
            constit = reverse_method(constit)
        x1 = constit[0]
        if constit[1] == 0 and constit[2] == 0:
            x23 = 0
        elif constit[1] == 0 and constit[2] == 1:
            x23 = 1
        elif constit[1] == 1 and constit[2] == 1:
            x23 = 2
        else:
            x23 = 3
        tabl[x1][x23] = 1


def str_form(formula, types):
    length_of_argu = 3
    ins, outs = str_form_tyoes(types)
    substr = []
    str_form_fro(formula, ins, length_of_argu, substr)
    outputs = outs.join(substr)
    return outputs



def change_table(tabl, type_of_formula):
    if type_of_formula == 'con':
        tabl = [reverse_method(rows) for rows in tabl]
        tabl = [[cell if cell == 0 else ' ' for cell in rows] for rows in tabl]
    else:
        tabl = [[cell if cell == 1 else ' ' for cell in rows] for rows in tabl]
    return tabl



def talbes(impls, constits):
    tabl = [['x' for ix in range(len(constits))] for jx in range(len(impls))]
    form_tables(constits, impls, tabl)
    return tabl


def form_tables(constits, impls, tabl):
    for impl in range(len(impls)):
        for con in range(len(constits)):
            for ix in range(number_of_arguments):
                if impls[impl][ix] != -1 and impls[impl][ix] != constits[con][ix]:
                    tabl[impl][con] = ' '





def str_form_tyoes(types):
    if types == 'dis':
        ins = '*'
        outs = '+'
    else:
        ins = '+'
        outs = '*'
    return ins, outs


def reverse_method(formula):
    reversed_formula = [1 if x == 0 else 0 for x in formula]
    return reversed_formula


def to_next(index, list_length):
    return (index + 1) % list_length


def to_quien(ix, table2, to_reduce):
    while ix < len(to_reduce):
        exc = True
        for jx in range(len(table2[ix])):
            if not (x_finder(table2, ix, jx)):
                exc = False
        if exc:
            to_reduce.pop(ix)
            table2.pop(ix)
        else:
            ix += 1


def method_table(formula, formtype):
    tabl = [[0 for jx in range(width_of_table)] for ix in range(height_of_table)]
    method_of_metod(formtype, formula, tabl)
    if formtype == 'con':
        for constit in formula:
            constit = reverse_method(constit)
    return tabl



def replacement(val, formula, formtype):
    argument_existing, result = sub(formula, val)
    if formula[argument_existing] == val[argument_existing]:
        if formtype == 'dis':
            result.append(1)
        else:
            result.append(0)
    else:
        if formtype == 'dis':
            result.append(0)
        else:
            result.append(1)
    return result



lines = input("Введите выражение: ")
truth = pp.truth_table(lines)
perfect = [pp.PDNF(truth), pp.PCNF(truth)]
for lines in perfect:
    formula = reading_line(lines)
    type_of_formula = types(lines)
    if type_of_formula == 'dis':
        str_impl = 'CДНФ: '
        final = 'ТДНФ: '
    else:
        str_impl = 'СКНФ: '
        final = 'ТКНФ: '
    impls = merg(formula)
    print('\n' + str_impl, end='')
    print(lines)
    if impls is not None:
        print('\nрасчетный метод:')
        to_reduce = excession_delete(impls, type_of_formula)
        reduced_again = merg2(to_reduce)
        print(str_impl + str_form(impls, type_of_formula))
        print(final + str_form(to_reduce, type_of_formula))
        print(final + str_form(reduced_again, type_of_formula))

        print('\n\nрасчетно-табличный метод:')
        constits = lines.split('+') if type_of_formula == 'dis' else lines.split('*')
        tablet = talbes(impls, formula)
        reduced2 = to_quin(tablet, impls)
        reduced_again2 = merg2(reduced2)
        print('\n\t\t\t\t\tконституенты')
        print('импликанты\t', end='')
        for constit in constits:
            print(constit.center(15), end='')
        print('')
        for ix in range(len(impls)):
            print(str_form([impls[ix]], type_of_formula).ljust(16), end='')
            for jx in range(len(tablet[ix])):
                print(tablet[ix][jx].center(15), end='')
            print('')
        print('\n' + final + str_form(reduced2, type_of_formula))
        print(final + str_form(reduced_again2, type_of_formula))

        print('\nтабличный метод:')
        tabl = method_table(formula, type_of_formula)
        impls = implicants(tabl, type_of_formula)
        print('\nx1^', end='')
        tabl = change_table(tabl, type_of_formula)
        ix = len(tabl) - 1
        while ix >= 0:
            print('\n' + str(ix) + ' |', end='  ')
            for jx in range(len(tabl[ix])):
                print(tabl[ix][jx], end='  ')
            ix -= 1
        print('\n   ------------->\n     00 01 11 10  x2 x3')
        print('\n' + final + str_form(impls, type_of_formula))
        reduced_again3 = merg2(impls)
        print(final + str_form(reduced_again3, type_of_formula))
    else:
        print('Не удалось склеить все конституенты')
