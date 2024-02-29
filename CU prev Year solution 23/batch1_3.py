def matrix_addition(matrix1, matrix2):
    result = []
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices should have the same dimensions for addition.")
        return None
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def matrix_subtraction(matrix1, matrix2):
    result = []
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices should have the same dimensions for subtraction.")
        return None
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Number of columns in matrix1 should be equal to number of rows in matrix2 for multiplication.")
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            val = 0
            for k in range(len(matrix2)):
                val += matrix1[i][k] * matrix2[k][j]
            row.append(val)
        result.append(row)
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Example matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matrix 1:")
print_matrix(matrix1)
print("\nMatrix 2:")
print_matrix(matrix2)

print("\nMatrix Addition:")
addition_result = matrix_addition(matrix1, matrix2)
print_matrix(addition_result)

print("\nMatrix Subtraction:")
subtraction_result = matrix_subtraction(matrix1, matrix2)
print_matrix(subtraction_result)

print("\nMatrix Multiplication:")
multiplication_result = matrix_multiplication(matrix1, matrix2)
print_matrix(multiplication_result)
