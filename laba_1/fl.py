def floating_sum(number_1, number_2):
    number_1 = converting_flout_to_bin_for_sun(number_1)
    number_2 = converting_flout_to_bin_for_sun(number_2)
    exp_1 = number_1.find(".") - number_1.find('1', 0, number_1.find(".")) - 1 if not number_1.find('1', 0, number_1.find(".")) == -1 else 0
    exp_2 = number_2.find(".") - number_1.find('1', 0, number_1.find(".")) - 1 if not number_1.find('1', 0, number_2.find(".")) == -1 else 0
    if exp_1 >= exp_2:
        diff_exp = exp_1 - exp_2
        number_summ2 = '0' * diff_exp + number_2[:(number_2.find("."))] + number_2[(number_2.find(".") + 1):(
                len(number_2) - diff_exp)]
        number_summ1 = number_1[:(number_1.find("."))] + number_1[(number_1.find(".") + 1):]
    else:
        diff_exp = exp_2 - exp_1
        number_summ1 = '0' * diff_exp + number_1[:(number_1.find("."))] + number_1[(number_1.find(".") + 1):(len(number_1) - diff_exp)]
        number_summ2 = number_2[:(number_2.find("."))] + number_2[(number_2.find(".") + 1):]
    temp_floating_summ = sum_diff_of_numbers(number_summ1, number_summ2)
    add_numbers = len(temp_floating_summ) - len(number_summ2)
    rez = temp_floating_summ[:(max(number_1.find("."), number_2.find("."))) + add_numbers] + "." + temp_floating_summ[(max(exp_1, exp_2) + add_numbers + 1):]
    rez = from_decimal_to_float(rez)
    return rez

def binAddCarry(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ''
    carry = 0
    flag = False

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

        carry = 0 if r < 2 else 1
    if carry != 0:
        flag = True
        return [result.zfill(max_len), flag]
    else:
        return [result.zfill(max_len), flag]


def fracToBin(n):
    binary = str()

    while (n):
        n *= 2

        if (n >= 1):
            int_part = 1
            n -= 1
        else:
            int_part = 0

        binary += str(int_part)
    return binary


def intTo32bin(n):
    sign_bit = 0

    if (n < 0):
        sign_bit = 1

    n = abs(n)

    int_str = bin(int(n))[2:32]

    fraction_str = fracToBin(n - int(n))

    if (n == 0):
        return ['0', '00000000', '00000000000000000000000']
    else:
        index = int_str.index('1')
        exponent = bin((len(int_str) - index - 1) + 127)[2:]
        exponent = '0' * (8 - len(exponent)) + exponent
        mantissa = int_str[index + 1:23] + fraction_str
        mantissa = mantissa + ('0' * (23 - len(mantissa)))
        if (len(mantissa) > 23):
            mantissa = bin(int(mantissa[0:23], 2) + 1)[2:]
            mantissa = '0' * (23 - len(mantissa)) + mantissa
        return [sign_bit, exponent, mantissa]


def binDiv(num1, num2):
    if (num2 == 0):
        print("Деление на 0 запрещено!")
    elif (num1 == 0):
        return intTo32bin(0.0)
    else:
        num1, num2 = intTo32bin(num1), intTo32bin(num2)
        print("\t" + str(num1[0]) + " | " + num1[1] + " | " + num1[2] + "\n/\t" +
              str(num2[0]) + " | " + num2[1] + " | " + num2[2])
        print("-" * 42)
        temp1 = '1' + num1[2]
        temp2 = '1' + num2[2]
        mantissa = int(temp1, 2) / int(temp2, 2)

        tmp = 0
        if mantissa < 1:
            mantissa += 1
            tmp = 1

        mantissa = intTo32bin(mantissa)
        mantissa = mantissa[2]
        exponent = bin(int(num1[1], 2) - int(num2[1], 2) + 127 - tmp)[2:]
        exponent = '0' * (8 - len(exponent)) + exponent
        signbit = num1[0] ^ num2[0]
        return [signbit, exponent, mantissa]

def compute_floating_point_sum(number_1, number_2):
    def get_exp(number):
        first_one = number.find('1', 0, number.find("."))
        return number.find(".") - first_one - 1 if first_one != -1 else 0

    number_1 = converting_flout_to_bin_for_sun(number_1)
    number_2 = converting_flout_to_bin_for_sun(number_2)

    exp_1 = get_exp(number_1)
    exp_2 = get_exp(number_2)

    if exp_1 >= exp_2:
        diff_exp = exp_1 - exp_2
        number_summ2 = '0' * diff_exp + number_2[:number_2.find(".")] + number_2[(number_2.find(".") + 1):]
        number_summ1 = number_1[:number_1.find(".")] + number_1[(number_1.find(".") + 1):]
    else:
        diff_exp = exp_2 - exp_1
        number_summ1 = '0' * diff_exp + number_1[:number_1.find(".")] + number_1[(number_1.find(".") + 1):]
        number_summ2 = number_2[:number_2.find(".")] + number_2[(number_2.find(".") + 1):]

    temp_floating_summ = sum_diff_of_numbers(number_summ1, number_summ2)
    add_numbers = len(temp_floating_summ) - len(number_summ2)

    rez = (
        temp_floating_summ[:(max(number_1.find("."), number_2.find("."))) + add_numbers] +
        "." +
        temp_floating_summ[(max(exp_1, exp_2) + add_numbers + 1):]
    )

    rez = from_decimal_to_float(rez)
    return rez

def converting_flout_to_bin_for_sun(number):
    if number == 0:
        return 0
    first_part = int(number)
    iterator = 0
    mantissa_size = 25
    point_part = number - float(first_part)
    second_part = dec_to_bin_add(first_part)
    if second_part.find('1') == -1:
        result = '0' + "."
    else:
        result = second_part[second_part.find('1'):] + "."
    while iterator <= (mantissa_size - len(result)):
        point_part *= 2
        if int(point_part) == 0:
            result += '0'
        elif int(point_part) == 1:
            point_part -= 1
            result += '1'
            if point_part == 0:
                result = result.ljust(23, '0')
    return result


def sum_diff_of_numbers(bin_num_1, bin_num_2):
    rez = ""
    number = 0
    bin_num_1, bin_num_2 = comparing_length(bin_num_1, bin_num_2)
    for i in reversed(range(len(bin_num_1))):
        if int(bin_num_1[i]) + int(bin_num_2[i]) == 1 and number == 0:
            rez = '1' + rez
        elif int(bin_num_1[i]) + int(bin_num_2[i]) == 1 and number > 0:
            rez = '0' + rez
        elif int(bin_num_1[i]) + int(bin_num_2[i]) == 2 and number > 0:
            rez = '1' + rez
        elif int(bin_num_1[i]) + int(bin_num_2[i]) == 0 and number > 0:
            rez = '1' + rez
            number -= 1
        elif int(bin_num_1[i]) + int(bin_num_2[i]) == 0 and number == 0:
            rez = '0' + rez
        elif int(bin_num_1[i]) + int(bin_num_2[i]) == 2 and number == 0:
            rez = '0' + rez
            number += 1

    if number > 0:
        rez = '1' + rez

    return rez


def from_decimal_to_float(float_num):
    if '1' in float_num[:float_num.find(".")]:
        exp_sign = 1
    else:
        exp_sign = -1
    sign_bit = '0'
    if float_num.find('1', 0, float_num.find(".")) == -1:
        exp_bits = dec_to_bin_straight(127 + (float_num.find('1') - float_num.find(".")) * exp_sign)[-8:]
    else:
        exp_bits = dec_to_bin_straight(127 + (float_num.find(".") - float_num.find('1') - 1) * exp_sign)[-8:]
    float_num = float_num[:float_num.find(".")] + float_num[float_num.find(".") + 1:]
    mantissa = float_num[float_num.find('1') + 1:]
    rez = sign_bit + " " + exp_bits + " " + mantissa
    return rez


def converte(num):
    sinal = 0 if num > 0 else 1
    num = num if num > 0 else num * -1
    temp = num
    expoente = 0

    if num > 1:
        while num != 1:
            temp = temp / 2
            num = num // 2
            expoente += 1
    else:
        while num < 1:
            temp = temp * 2
            num = temp
            expoente -= 1
    temp = temp - 1
    mantissa = ''
    if temp > 0 and temp < 1:
        while temp != 1:
            temp = temp * 2
            if temp > 1:
                temp = temp - 1
                mantissa = mantissa + str(1)
            elif temp == 1:
                mantissa = mantissa + str(1)
            else:
                mantissa = mantissa + str(0)
    while len(mantissa) < 23:
        mantissa = mantissa + str(0)
    iee = str(sinal) + ' ' + str(expoente) + ' ' + str(mantissa)


def dec_to_bin_straight(float_num):
    bin_num = ""
    tick_of_actions, clone_of_dec_num, tick_of_bits = 0, float_num, 0
    rez = ""
    bit_size = 8 if abs(float_num) < 100 else 8 * 2
    if float_num < 0:
        clone_of_dec_num = -float_num
    if float_num == 0:
        bin_num = str(0)
    while clone_of_dec_num >= 1:
        symbol = str(int(clone_of_dec_num % 2))
        bin_num += symbol
        tick_of_bits += 1
        clone_of_dec_num /= 2
        tick_of_actions += 1
        rez = bin_num[::-1]
    if tick_of_bits < bit_size:
        rez = rez.zfill(bit_size)
    if float_num < 0:
        rez = str(1) + rez[1:]
    else:
        rez = str(0) + rez[1:]
    return rez



def dec_to_bin_add(float_num):
    if float_num < 0:
        rez = dec_to_bin_rev(float_num)
        iterator = 1
        help_add = True
        while help_add:
            temp_rez = rez[-iterator:]
            if rez[-iterator] == '0':
                temp_rez = temp_rez.replace('1', '0').replace('0', '1').replace('2', '0')
                rez = rez[:-iterator] + temp_rez
                help_add = False
            else:
                iterator += 1
    else:
        rez = dec_to_bin_straight(float_num)
    return rez


def dec_to_bin_rev(float_num):
    sign = '1' if float_num < 0 else '0'
    rez = dec_to_bin_straight(float_num)
    rez = rez.replace('1', '0').replace('0', '1').replace('2', '0')
    rez = sign + rez[1:]
    return rez


def comparing_length(bin_num1, bin_num2):
    max_size = max(len(bin_num1), len(bin_num2))
    if bin_num1[0] == bin_num2[0] == '0':
        bin_num1 = bin_num1.zfill(max_size)
        bin_num2 = bin_num2.zfill(max_size)
    if bin_num1[0] == '1':
        bin_num1 = bin_num1.rjust(max_size, '1')
    if bin_num2[0] == '1':
        bin_num2 = bin_num2.rjust(max_size, '1')
    return bin_num1, bin_num2


def float_to_decimal_conversion(float_num):
    float_num = float_num[:float_num.find(" ")] + float_num[(float_num.find(" ") + 1):float_num.rfind(" ")] + float_num[float_num.rfind(" ") + 1:]
    decimal_mantissa = 0.0
    for i in range(9, len(float_num)):
        decimal_mantissa += int(float_num[i]) * pow(2, -(i - 8))
    exp = int(from_binary_to_decimal('0' + float_num[1:9])) - 127
    sign_before = "-" if float_num[0] == '1' else ""
    rez = sign_before + str((1 + decimal_mantissa) * pow(2, exp))
    return rez


def from_binary_to_decimal(bin_num):
    rez = 0
    if bin_num.startswith('1'):
        rez -= int(bin_num[1]) * pow(2, len(bin_num) - 2)
        for iterator in range(2, len(bin_num)):
            rez += int(bin_num[iterator]) * pow(2, len(bin_num) - (iterator + 1))
    elif bin_num.startswith('0'):
        for iterator in range(len(bin_num)):
            rez += int(bin_num[iterator]) * pow(2, len(bin_num) - (iterator + 1))
    return rez


def convert_string_to_list(bin_num):
    rez = []
    for i in range(len(bin_num)):
        if bin_num[i] == ' ':
            continue
        rez.append(bin_num[i])
    return rez