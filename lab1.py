

def summa(number_1, number_2):
    index = len(number_1) - 1
    result = []
    while index > -1:
        if number_1[index] + number_2[index] < 2:
            result.insert(0, number_1[index] + number_2[index])
        else:
            result.insert(0, number_1[index] + number_2[index] - 2)
            if index > 0:
                number_1[index - 1] = number_1[index - 1] + 1
        index = index - 1
    return result


def subtract_numbers(number_1, number_2):
    number2 = number_2.copy()

    number1 = number_1.copy()

    while len(number2) < len(number1):
        number2.insert(0, 0)
    number1.insert(0, 0)
    number2.insert(0, 1)
    number2 = add_one(swap(number2))
    result = summa(number1, number2)
    result.pop(0)
    return result

def compare_numbers(number1, number2):
    ix = 0
    num2 = number2.copy()
    if len(number1) < len(number2):
        return False
    while len(number1) > len(num2):
        num2.insert(0, 0)
    while ix < len(number1):
        if number1[ix] > num2[ix]:
            return True
        elif number1[ix] == num2[ix]:
            ix += 1
        else:
            return False
    return True


def mantissa_sum(mantissa_1, mantissa_2, sign_1, sign_2):
    result_m = summa(mantissa_1, mantissa_2)
    if result_m[0] == 1:
        result_m = add_one(swap(result_m))
    if sign_2 == 1:
        mantissa_2 = add_one(swap(mantissa_2))
        mantissa_2[0] = 1
    if sign_1 == 1:
        mantissa_1 = add_one(swap(mantissa_1))
        mantissa_1[0] = 1
    return result_m


def floating_point_sum(num_1, num_2):
    exponent_1 = binary_to_decimal(get_exponent(num_1))
    exponent_2 = binary_to_decimal(get_exponent(num_2))
    mantissa_1 = [0, 0, 1] + get_mant(num_1)
    mantissa_2 = [0, 0, 1] + get_mant(num_2)
    diff = abs(exponent_1 - exponent_2)
    result_exponent = get_exponent(num_1)

    if diff != 0:
        if exponent_1 > exponent_2:
            mantissa_2 = shifter(mantissa_2, diff)
        else:
            result_exponent = get_exponent(num_2)
            mantissa_1 = shifter(mantissa_1, diff)

    result_mantissa = mantissa_sum(mantissa_1, mantissa_2, num_1[0], num_2[0])
    sign = 0

    if result_mantissa[0] == 1:
        sign = 1
    result_mantissa.pop(0)

    if result_mantissa[0] == 1:
        result_mantissa = shifter(result_mantissa, 1)
        result_exponent = add_one(result_exponent)
    elif result_mantissa[1] == 0:
        while result_mantissa[1] == 0:
            result_mantissa.pop(0)
            result_mantissa.append(0)
            result_exponent = subtract_numbers(result_exponent, [1])

    result_mantissa.pop(0)
    result_mantissa.pop(0)

    return [sign] + result_exponent + result_mantissa

def opposite(number_decart):
    ix=0
    number_bin = dec_to_bin(number_decart)
    ix=-1

    return swap(number_bin)

def swap(binar_number):
    result = [0] * len(binar_number)
    result[0] = binar_number[0]
    ix = 1
    while ix < len(binar_number):
        if binar_number[ix] == 0:
            result[ix] = 1
        else:
            result[ix] = 0
        ix -= 1
        ix += 2
    return result

def add_binary_numbers1():
    global add_binary_numbers

    def add_binary_numbers(number_1, number_2, flags):
        length = len(number_1)
        result = [0 for _ in range(length)]
        carry = 0

        for ix in range(length - 1, -1, -1):
            total = number_1[ix] + number_2[ix] + carry

            if total < 2:
                result[ix] = total
                carry = 0
            else:
                result[ix] = total - 2
                carry = 1

            if ix == 0 and flags and carry == 1:
                result = add_one(result)

        return result


add_binary_numbers1()

def integerr(number_bin):
    length = len(number_bin)
    ix = 1
    number_decart = 0

    while ix < length:
        number_decart = number_decart + (2 ** (length - 1 - ix)) * number_bin[ix]
        ix = ix + 1

    if number_bin[0] == 1:
        number_decart = -number_decart

    return number_decart

def binary_to_decimal(binary_num):
    decimal_num = 0
    power = 0

    for ix in range(len(binary_num) - 1, -1, -1):
        decimal_num += binary_num[ix] * (2 ** power)
        power += 1

    return decimal_num

def decimal_to_binary(numberr):
    binary_list = []

    while numberr > 0:
        binary_list.insert(0, numberr % 2)
        numberr //= 2

    return binary_list

def product(number_1, number_2):
    result = [0] * (len(number_1) + len(number_2))
    number_2_extended = [0] + number_2 + [0]

    for ix, bit in enumerate(number_1):
        if bit == 1:
            partial_product = [0] * len(number_2_extended)
            for j, digit in enumerate(number_2_extended):
                partial_product[j] = digit + (ix * digit)
            result = summa(result, partial_product)

    return result


def divide1():
    global divide

    def divide(number_1, number_2):
        quotient = []
        remainder = number_1.copy()

        while len(remainder) >= len(number_2) and compare_numbers(remainder, number_2) and remainder != [0]:
            counter = 1
            while len(remainder) > len(number_2):
                number_2.append(0)
                counter += 1

            digit = 0
            while compare_numbers(remainder, number_2):
                digit += 1
                remainder = subtract_numbers(remainder, number_2)

            quotient.append(digit)
            number_2.pop()

        if len(quotient) == 0:
            quotient = [0]

        fractil_part = divide_fraction(remainder, number_2)
        return quotient, fractil_part


divide1()

def convert_to_floating2(array, fractional_part, exponent, sign, power_negative):
    exponent_shift = 127
    mantissa_length = 23

    while len(array) < mantissa_length + 1:
        if fractional_part >= power_negative:
            array.append(1)
            fractional_part = fractional_part - power_negative
        else:
            array.append(0)
        power_negative = power_negative / 2

    array.pop(0)
    exponent = exponent_shift + exponent
    ix = 0
    while ix < 8:
        if exponent >= 2 ** (7 - ix):
            array.insert(ix, 1)
            exponent = exponent - 2 ** (7 - ix)
        else:
            array.insert(ix, 0)
        ix = ix + 1

    array.insert(0, sign)
    return array

def round_number1():
    global round_number

    def round_number(num):
        digits = 5
        bases = 10
        number_str = str(num)
        dot_index = number_str.find('.')

        if dot_index == -1 or len(number_str) <= digits:
            return float(number_str)

        if int(number_str[digits]) >= 5:
            is_plus = True
        else:
            is_plus = False

        num = float(number_str[:digits])

        if is_plus:
            if dot_index != -1:
                exponent = dot_index - digits
            else:
                exponent = 0
            num += bases ** exponent

        return num


round_number1()



def convert_to_floating(number):
    parts = number.split('.')
    part_integer = int(parts[0])

    part_fractional = float('0.' + parts[1])
    power_negative = 0.5

    signs = 1 if number[0] == '-' else 0

    if part_integer != 0:
        binary_arr = decimal_to_binary(part_integer)

        exponent = len(binary_arr) - 1       #может поможет может нет

    else:
        binary_arr = []
        exponent = -1
        while part_fractional < power_negative:
            exponent -= 1

            power_negative /= 2
    return convert_to_floating2(binary_arr, part_fractional, exponent, signs, power_negative)

def convert_to_floating2(array, fractional_part, exponent, signs, power_negative):
    exp_shift = 127
    mant_len = 23
    while len(array) < mant_len+1:
        if fractional_part >= power_negative:
            array.append(1)
            fractional_part = fractional_part - power_negative
        else:
            array.append(0)
        power_negative = power_negative/2
    array.pop(0)
    exponent = exp_shift + exponent
    ix = 0
    while ix < 8:
        if exponent >= 2**(7-ix):
            array.insert(ix,1)
            exponent = exponent - 2**(7-ix)
        else:
            array.insert(ix,0)
        ix = ix + 1
    array.insert(0,signs)
    return array

def increment_by_one(index):
    if index >= 0:
        return dec_to_bin(index)
    else:
        return add_one(opposite(index))

def add_one(binar_number):
    first = [0 for ix in range(len(binar_number))]
    first[len(binar_number)-1] = 1
    return summa(binar_number, first)



def get_exponent(float_number):
    exponent_end = 9

    index = 1
    exponent = []
    while index < exponent_end:
        exponent.append(float_number[index])

        index += 1

    return exponent

def get_mant(float_number):
    exponent_end = 9
    tot_bits = 32

    mant = []


    while exponent_end < tot_bits:
        mant.append(float_number[exponent_end])
        exponent_end += 1

    return mant


def shifter(binary_number, num_shift):
    index = 0
    result = []

    while index < num_shift:
        result.append(0)
        index += 1
    while index < len(binary_number):
        result.append(binary_number[index - num_shift])
        index += 1
    return result




def float_to_decimal(bin_arr):
    index = 1
    exponent = 0
    mantissa = 0
    mantissa_shift = 127
    mantissa_bits = 23
    total_bits = 32
    exponent_bits = 8

    while index < 9:
        exponent = exponent + (2 ** (exponent_bits - index)) * bin_arr[index]
        index = index + 1

    while index < total_bits:
        mantissa = mantissa + (2 ** (total_bits - index - 1)) * bin_arr[index]
        index = index + 1

    decimal = 2 ** (exponent - mantissa_shift) * (1 + mantissa / 2 ** mantissa_bits)

    if bin_arr[0] == 1:
        decimal = -decimal

    return decimal
def dec_to_bin1():
    global dec_to_bin

    def dec_to_bin(number_decart):
        num_bits = 8
        binary_representation = [0] * num_bits

        if number_decart < 0:
            binary_representation[0] = 1
            number_decart = abs(number_decart)

        for ix in range(num_bits - 1, -1, -1):
            if number_decart >= 2 ** ix:
                binary_representation[num_bits - ix - 1] = 1
                number_decart -= 2 ** ix

        return binary_representation


dec_to_bin1()
def divide_fraction(number_1, number_2):
    quotient = []
    for _ in range(30):
        number_1.append(0)

        if compare_numbers(number_1, number_2):
            number_1 = subtract_numbers(number_1, number_2)
            quotient.append(1)

        else:
            quotient.append(0)
    return quotient



def perform_addition(a, b):
    if a >= 0 and b >= 0:
        a_binary = decimal_to_binary(a)
        b_binary = decimal_to_binary(b)
        print('a: ' + str(a_binary))
        print('b: ' + str(b_binary))
        result = add_binary_numbers(a_binary, b_binary, True)
    elif a < 0 and b < 0:
        a_opposite = opposite(a)
        b_opposite = opposite(b)
        print('a:   ' + str(a_opposite))
        print('b:   ' + str(b_opposite))
        result = add_binary_numbers(a_opposite, b_opposite, True)
        result = swap(result)
    else:
        c = a + b
        a_incremented = increment_by_one(a)
        b_incremented = increment_by_one(b)
        print('a: ' + str(a_incremented))
        print('b: ' + str(b_incremented))
        result = add_binary_numbers(a_incremented, b_incremented, False)
        if c < 0:
            result = add_one(swap(result))
    print('res: ' + str(result))
    print('integer res: ' + str(integerr(result)))


def perform_multiplication(a, b):
    signs = 0
    if a < 0:
        signs += 1
        a = -a
    if b < 0:
        signs += 1
        b = -b
    a_binary = decimal_to_binary(a)
    b_binary = decimal_to_binary(b)
    print('a:   ' + ''.join(str(el) for el in a_binary))
    print('b:   ' + ''.join(str(el) for el in b_binary))
    result = product(a_binary, b_binary)
    print('res: ' + ''.join(str(el) for el in result))
    result = binary_to_decimal(result)
    if signs == 1:
        result = -result
    print('integer res: ' + str(result))


def perform_division(a, b):
    signs = 0
    if a < 0:
        signs += 1
        a = -a
    if b < 0:
        signs += 1
        b = -b
    a_binary = decimal_to_binary(a)
    b_binary = decimal_to_binary(b)
    print('a:   ' + ''.join(str(el) for el in a_binary))
    print('b:   ' + ''.join(str(el) for el in b_binary))
    int_part, fractional_part = divide(a_binary, b_binary)
    result = binary_to_decimal(int_part) + binary_to_decimal(fractional_part) / 2**30
    str_res = ''.join(str(el) for el in int_part) + '.' + ''.join(str(el) for el in fractional_part)
    print('res: ' + str_res)
    result = round_number(result)
    if signs == 1:
        result = -result
    print('integer res: ' + str(result))


def perform_floating_point_sum(a, b):
    print('a:    s= ' + str(a[0]) + '  exponent= ' + ''.join(str(a[ix]) for ix in range(1, 9))
          + '  m= ' + ''.join(str(a[ix]) for ix in range(10, 32)))
    print('b:    s= '+ str(b[0]) + '  exponent= ' + ''.join(str(b[ix]) for ix in range(1, 9))
          + '  m= ' + ''.join(str(b[ix]) for ix in range(10, 32)))
    result = floating_point_sum(a, b)
    print('res:  s= ' + str(result[0]) + '  exponent= ' + ''.join(str(result[ix]) for ix in range(1, 9))
          + '  m= ' + ''.join(str(result[ix]) for ix in range(10, 32)))
    print('integer res: ' + str(float_to_decimal(result)))


while True:
    opt = input('выберите операцию\n1 - сложение\n2 - умножение\n3 - деление\n4 - сложение с плавающей точкой\n')
    match opt:
        case '1':
            a = int(input('input а: '))
            b = int(input('input b: '))
            perform_addition(a, b)
        case '2':
            a = int(input('input а: '))
            b = int(input('input b: '))
            perform_multiplication(a, b)
        case '3':
            a = int(input('input а: '))
            b = int(input('input b: '))
            perform_division(a, b)
        case '4':
            a = input('input а: ')
            b = input('input b: ')
            a_floating = convert_to_floating(a)
            b_floating = convert_to_floating(b)
            perform_floating_point_sum(a_floating, b_floating)

