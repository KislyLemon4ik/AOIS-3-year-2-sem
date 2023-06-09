from converting import *
from mult import amount
from amount import len_alignment


def consider(bin_1: list):
    dec_num = 0
    for bit in bin_1:
        if bit == '0':
            dec_num += 1
        elif bit == '1':
            break
    return dec_num

def integer2binary(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def splitting(dec_1: int, dec_2: int):
    bin_t1, bin_2, sizes = len_alignment(converting(dec_1), converting(dec_2))
    bin_t2 = dopp(refund(bin_2))
    if not len(bin_t2) == sizes:
        bin_t2 = bin_t2[::-1]
    while not len(bin_t2) == sizes:
        bin_t2 += '0'
        bin_t2 = bin_t2[::-1]
        result = ['0'] * sizes
        edd = ['0'] * (sizes - 1) + ['1']
        one = consider(bin_t1)
        second = consider(bin_2)
    while one <= second:
        bin_t1 = amount(bin_t1, bin_t2)
        result = amount(edd, result)
        one = consider(bin_t1)
    return result

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
