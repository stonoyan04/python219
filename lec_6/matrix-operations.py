import random

def generate_random_matrix(rows, cols):
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

def get_column_sum(matrix, col_index):
    return sum(row[col_index] for row in matrix)

def get_row_average(matrix, row_index):
    return sum(matrix[row_index]) / len(matrix[row_index])

matrix = generate_random_matrix(4, 5)
print("Generated Matrix:")
for row in matrix:
    print(row)

column_sum = get_column_sum(matrix, 2)
print(f"Sum of column 2: {column_sum}")

row_avg = get_row_average(matrix, 1)
print(f"Average of row 1: {row_avg}")