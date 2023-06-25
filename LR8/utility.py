import QuadraticMatrix
from boolean_operations import *


def search(matrix: QuadraticMatrix, index):
    print(matrix[index])


def setter(matrix: QuadraticMatrix, value, index):
    matrix[index] = value


def summa(arg1, arg2):
    answer = [0, 0, 0, 0, 0]
    transfer = 0
    for x in range(len(arg1)-1, -1, -1):
        if arg1[x] + arg2[x] + transfer == 0:
            answer[x+1] = 0
        if arg1[x] + arg2[x] == 1:
            if transfer == 0:
                answer[x+1] = 1
            if transfer == 1:
                answer[x+1] = 0
        if arg1[x] + arg2[x] == 2:
            if transfer == 1:
                answer[x+1] = 1
            if transfer == 0:
                transfer = 1
                answer[x+1] = 0
    if transfer == 1:
        answer[0] = 1
    return answer


def sum(V, array):
    for x in range(array.SIZE):
        if V[:3] == array[x][:3]:
            word1 = array[x][3:7]
            word2 = array[x][7:11]
            array[x][11:16] = summa(word1, word2)



def search_max(array):
    answer = []
    adding = [1 for _ in range(len(array))]
    for x in range(len(array[0])):
        value = 0
        for y in range(len(array)):
            if array[y][x] == 1 and adding[y] == 1:
                value = 1
                break
        for y in range(len(array)):
            if value == 1:
                if array[y][x] != 1:
                    adding[y] = 0
        for y in range(len(array)):
            if value == 1 and adding[y] == 1:
                answer.append(1)
                break
            if value == 0 and adding[y] == 1:
                answer.append(0)
                break
    return answer


def search_min(array):
    answer = []
    adding = [1 for _ in range(len(array))]
    for x in range(len(array[0])):
        value = 1
        for y in range(len(array)):
            if array[y][x] == 0 and adding[y] == 1:
                value = 0
                break
        for y in range(len(array)):
            if value == 0:
                if array[y][x] != 0:
                    adding[y] = 0
        for y in range(len(array)):
            if value == 0 and adding[y] == 1:
                answer.append(0)
                break
            if value == 1 and adding[y] == 1:
                answer.append(1)
                break
    return answer


def sort(array, flag):
    result = []
    arr = array[:]
    if flag == 'min':
        while len(arr) > 0:
            min = search_min(arr)
            result.append(min)
            arr.remove(min)
    if flag == 'max':
        while len(arr) > 0:
            max = search_max(arr)
            result.append(max)
            arr.remove(max)
    return result


def print_list(array):
    print('_____________________Table______________________')
    for x in range(len(array)):
        print(array[x])


def logical_operation(index1, index2, operation, array):
    if operation == 'f4':
        print(array[index1])
        print(array[index2])
        array[index2] = operation_f4(array[index1], array[index2])
        print(array[index2])
    if operation == 'f9':
        print(array[index1])
        print(array[index2])
        array[index2] = operation_f9(array[index1], array[index2])
        print(array[index2])
    if operation == 'f6':
        print(array[index1])
        print(array[index2])
        array[index2] = operation_f6(array[index1], array[index2])
        print(array[index2])
    if operation == 'f11':
        print(array[index1])
        print(array[index2])
        array[index2] = operation_f11(array[index1], array[index2])
        print(array[index2])
