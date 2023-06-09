from amount import *


def amount(bin_1: list, bin_2: list):
    number = '0'
    rez = []
    for i in reversed(range(len(bin_1))):
        if bin_1[i] == '0' and bin_2[i] == '0':
            if number == '1':
                rez += '1'
                number = '0'
                continue
            rez += '0'
            number = '0'
        elif bin_1[i] == '1' and bin_2[i] == '1':
            if number == '1':
                rez += '1'
                number = '1'
                continue
            rez += '0'
            number = '1'
        elif (bin_1[i] == '0' and bin_2[i] == '1') or (bin_1[i] == '1' and bin_2[i] == '0'):
            if number == '1':
                rez += '0'
                number = '1'
                continue
            rez += '1'
            number = '0'

    return rez[::-1]

def splitting(bin_1: list, bin_2: list):
    rez = []
    carry = '0'
    for i in reversed(range(len(bin_1))):
        if bin_1[i] == bin_2[i]:
            rez.append(carry)
            carry = bin_1[i]
        else:
            rez.append('1' if carry == '0' else '0')

    if carry == '1':
        rez.append('1')

    return rez[::-1]

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

def diff(dec_1: int, dec_2: int):
    bin_1, bin_2, size = len_alignment(converting(dec_1), converting(dec_2))
    rez = ['0'] * size

    for i in reversed(range(size)):
        if bin_2[i] == '1':
            num = ['0'] * (size - i - 1) + bin_1[::-1]
            rez = amount(rez[::-1], num[::-1])[::-1]

    return rez

def mult(dec_1: int, dec_2: int):
    bin_1, bin_2, size = len_alignment(converting(dec_1), converting(dec_2))
    rez = []
    for i in range(size):
        rez += '0'
    null = 0
    for i in reversed(range(size)):
        num = []
        if bin_2[i] == '0':
            null += 1
        elif bin_2[i] == '1':
            for j in range(null):
                num += '0'
            num += bin_1[::-1]
            num = num[::-1]
            rez = rez[::-1]
            for t in range(len(num)-len(rez)):
                rez += '0'
            rez = rez[::-1]
            rez = amount(rez, num)
            null += 1

    return rez


while (True):

    """ Função: sinal_iee():
     *  Apresentação => Fornece o sinal do número convertido
     *  return => 1 = Negativo | 0 = Positivo
    """


    def sinal_iee():
        if int(entrada, 16) >= 0:
            sinal = 0
        else:
            sinal = 1
        return sinal


    """ Função expoente_iee():
     *  Apresentação => Calcula o expoente da conversão IEE
     *  return => Expoente do IEE
    """


    def expoente_iee():
        bias = 127
        bin_expoente = bin((bias + (len(entrada_binario) - 3)))
        expoente = (str(bin_expoente))[2:(len(bin_expoente))]
        return expoente


    """ Função mantissa_iee():
     *  Apresentação => Calcula a mantissa da conversão IEE
     *  return => Valor da mantissa
    """


    def mantissa_iee():
        mantissa = entrada_binario[3:(len(entrada_binario))]
        while (30):
            mantissa = mantissa + mantissa
            if len(mantissa) > 23:
                mantissa = mantissa[0:23]
                break
        return mantissa


    print("Выберите операцию:")
    print("0 --> Выход")
    print("1 --> Сумма")
    print("2 --> Разность")
    print("3 --> Произведение")
    print("4 --> Деление")
    print("5 --> Получить сумму")
    entrada = '0x' + input("Выберите операцию:")

    entrada_binario = bin(int(entrada, 16))

    sinal = sinal_iee()
    expoente = expoente_iee()
    mantissa = mantissa_iee()

    print(sinal, expoente, mantissa)

    while (True):

        resposta = (input('Введите первое число: '))+ (input('Введите второе число: '))

        if resposta == 'N':
            continuar = 'N'
            break
        elif resposta == 'Y':
            continuar = 'Y'
            break

    if continuar == 'N':
        break