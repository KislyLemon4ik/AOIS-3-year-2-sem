from enum import Enum
from QuadraticMatrix import *
import utility as ut


class Operation(Enum):
    SHOW_MATRIX = "1"
    SHOW_DIAGONAL_MATRIX = "2"
    READ_BY_INDEX = "3"
    SEARCH_BY_INDEX = "4"
    SET_VALUE_BY_INDEX = "5"
    SORT = "6"
    SUM_BY_KEY = "7"
    BOOLEAN_OPERATIONS = "8"


matrix = QuadraticMatrix()
matrix.fill_matrix()
matrix.print_matrix()

vertical_matrix = QuadraticMatrix.vertical_swap(matrix)

while True:
    operation = input("1 - показать матрицу\n"
                      "2 - диагональный вид\n"
                      "3 - чтение по индексу в диагональной матрице\n"
                      "4 - поиск по индексу\n"
                      "5 - установка значения по индексу\n"
                      "6 - сортировка\n"
                      "7 - сумма по ключу\n"
                      "8 - булевые операции\n")
    match operation:
        case Operation.SHOW_MATRIX.value:
            matrix.print_matrix()
        case Operation.SHOW_DIAGONAL_MATRIX.value:
            vertical_matrix.print_matrix()
        case Operation.READ_BY_INDEX.value:
            print(QuadraticMatrix.get_vertical_word(vertical_matrix, 0))
        case Operation.SEARCH_BY_INDEX.value:
            ut.search(matrix, 1)
        case Operation.SET_VALUE_BY_INDEX.value:
            ut.setter(matrix, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
        case Operation.SORT.value:
            ut.print_list(ut.sort(matrix, 'max'))
        case Operation.SUM_BY_KEY.value:
            ut.sum([0, 0, 1], matrix)
            matrix.print_matrix()
        case Operation.BOOLEAN_OPERATIONS.value:
            print('1-2,f4')
            ut.logical_operation(1, 2, 'f4', matrix)
            matrix.print_matrix()

            print('1-3,f6')
            ut.logical_operation(1, 3, 'f6', matrix)
            matrix.print_matrix()

            print('1-4,f9')
            ut.logical_operation(1, 4, 'f9', matrix)
            matrix.print_matrix()

            print('1-5,f11')
            ut.logical_operation(1, 5, 'f11', matrix)
            matrix.print_matrix()
