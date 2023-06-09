from converting import *


def return_to_code(output: list):
    output = [str(1 - int(bit)) for bit in output]
    number = '1'
    for i in reversed(range(len(output))):
        if output[i] == '0' and number == '1':
            output[i] = '1'
            number = '0'

        elif output[i] == '1' and number == '1':
                output[i] = '0'
                output[0] = '1'
    return output

def len_alignment(bin_1: list, bin_2: list):
    size = max(len(bin_1), len(bin_2))
    bin_1 += ['0'] * (size - len(bin_1))
    bin_2 += ['0'] * (size - len(bin_2))
    return bin_1, bin_2, size

def str2hex(self) -> str:
        s = str(self)
        for i in range(0, len(s), 4):
            ss = s[i:i + 4]
            si = 0
            for j in range(4):
                si += int(ss[j]) * (2 ** (3 - j))
            sh = hex(si)
            self.h += sh[2]
        return self.h.capitalize()

def amount(dec_1: int, dec_2: int):
    bin_1, bin_2, size = len_alignment(converting(dec_1), converting(dec_2))
    output = []
    number = '0'
    for i in reversed(range(size)):
        if bin_1[i] == '0' and bin_2[i] == '0':
            if number == '1':
                output.append('1')
                number = '0'
            else:
                output.append('0')
        elif bin_1[i] == '1' and bin_2[i] == '1':
            if number == '1':
                output.append('1')
            else:
                output.append('0')
            number = '1'
        else:
            if number == '1':
                output.append('0')
            else:
                output.append('1')
                output.reverse()
    return output if output[0] == '0' else return_to_code(output)