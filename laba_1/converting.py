def converting(number):
    return straight(number) if number >= 0 else dopp(abs(number))


def straight(number):
    bb = []
    while number > 0:
        bb.append(str(number % 2))
        number //= 2

    while len(bb) % 8 != 0:
        bb.append('0')

    return ''.join(bb[::-1])


def dopp(number):
    bb = []
    while number > 0:
        bb.append(str(number % 2))
        number //= 2

    while len(bb) % 8 != 0:
        bb.append('0')

    bb1 = ['1' if bit == '0' else '0' for bit in bb[::-1]]

    number = '1'
    for i in range(len(bb1)):
        if bb1[i] == '0' and number == '1':
            bb1[i] = '1'
            number = '0'
        elif bb1[i] == '1' and number == '1':
            bb1[i] = '0'

    return ''.join(bb1[::-1])

def converting_float_to_bin_for_sun(number):
    if number == 0:
        return '0'

    first_part = int(number)
    mantissa_size = 25
    point_part = number - float(first_part)
    second_part = number(first_part)

    if second_part.find('1') == -1:
        result = '0' + "."
    else:
        result = second_part[second_part.find('1'):] + "."

    iterator = 0
    while iterator <= (mantissa_size - len(result)):
        point_part *= 2
        if int(point_part) == 0:
            result += '0'
        elif int(point_part) == 1:
            point_part -= 1
            result += '1'
            if point_part == 0:
                result = result.ljust(23, '0')

        iterator += 1

    return result

def bin32toInt(bin):
    signbit = bin[0]
    exponent = int(bin[1], 2) - 127
    mantissa = bin[2]
    mantissa_int = 0
    power_count = -1

    for i in mantissa:
        mantissa_int += (int(i) * pow(2, power_count))
        power_count -= 1
    mantissa_int += 1
    number = pow(-1, signbit) * mantissa_int * pow(2, exponent)
    return number



def refund(bb: list):
    aa = 0
    for i in range(len(bb) - 1, 0, -1):
        aa += (2 ** (len(bb) - i - 1)) * int(bb[i])
    if bb[0] == '1':
        aa = -aa
    return aa