import random


class QuadraticMatrix:
    SIZE = 16

    def __init__(self):
        self.matrix = [[0] * self.SIZE for _ in range(self.SIZE)]

    def __getitem__(self, indices):
        if isinstance(indices, tuple):
            row, col = indices
            return self.matrix[row][col]
        else:
            return self.matrix[indices]

    def __setitem__(self, indices, value):
        if isinstance(indices, tuple):
            row, col = indices
            self.matrix[row][col] = value
        else:
            self.matrix[indices] = value

    def fill_matrix(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                self.matrix[i][j] = random.randint(0, 1)

    def print_matrix(self):
        for row in self.matrix:
            print(' '.join(str(element) for element in row))

    @staticmethod
    def get_vertical_word(matrix: 'QuadraticMatrix', index) -> list:
        word = []
        for i in range(matrix.SIZE):
            another_i = i + index
            if another_i >= matrix.SIZE:
                another_i -= matrix.SIZE
            word.append(matrix[another_i, index])
        return word

    @staticmethod
    def vertical_swap(matrix: 'QuadraticMatrix') -> 'QuadraticMatrix':
        new_matrix = QuadraticMatrix()
        for i in range(new_matrix.SIZE):
            for j in range(new_matrix.SIZE):
                new_j = j + i
                if new_j >= new_matrix.SIZE:
                    new_j = j + i - new_matrix.SIZE
                new_matrix[new_j, i] = matrix[i, j]
        return new_matrix
