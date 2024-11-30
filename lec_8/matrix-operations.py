import random


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]

    def print_matrix(self):
        print("Matrix:")
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
        total_elements = self.n * self.m
        total_sum = sum(sum(row) for row in self.matrix)
        return total_sum / total_elements

    def sum_of_row(self, row_index):
        if 0 <= row_index < self.n:
            return sum(self.matrix[row_index])
        else:
            raise IndexError("Row index out of range.")

    def average_of_column(self, col_index):
        if 0 <= col_index < self.m:
            col_sum = sum(self.matrix[i][col_index] for i in range(self.n))
            return col_sum / self.n
        else:
            raise IndexError("Column index out of range.")

    def submatrix(self, col1, col2, row1, row2):
        if 0 <= row1 <= row2 < self.n and 0 <= col1 <= col2 < self.m:
            print("Submatrix:")
            for i in range(row1, row2 + 1):
                print(self.matrix[i][col1:col2 + 1])
        else:
            raise IndexError("Submatrix indices out of range.")


if __name__ == "__main__":
    n = int(input("Enter the number of rows for the matrix: "))
    m = int(input("Enter the number of columns for the matrix: "))

    matrix = Matrix(n, m)

    matrix.print_matrix()

    print("Mean of the matrix:", matrix.calculate_mean())

    row_index = int(input(f"Enter the row index (0 to {n - 1}) to calculate the sum: "))
    try:
        print(f"Sum of row {row_index}:", matrix.sum_of_row(row_index))
    except IndexError as e:
        print(e)

    col_index = int(input(f"Enter the column index (0 to {m - 1}) to calculate the average: "))
    try:
        print(f"Average of column {col_index}:", matrix.average_of_column(col_index))
    except IndexError as e:
        print(e)

    print("Enter the indices for the submatrix (inclusive, 0-based):")
    col1 = int(input("Enter starting column index (col1): "))
    col2 = int(input("Enter ending column index (col2): "))
    row1 = int(input("Enter starting row index (row1): "))
    row2 = int(input("Enter ending row index (row2): "))
    try:
        matrix.submatrix(col1, col2, row1, row2)
    except IndexError as e:
        print(e)