inp1 = input()  # reads in the matrix
inp1_strip = inp1.strip("(),[] ")  # removes brackets or parantheses and spaces
matrix1 = [list(map(float, t.split(","))) for t in inp1_strip.split(";")]  # creates a matrix for input

inp2 = input()  # reads in the second matrix
inp2_strip = inp2.strip("(),[] ")  # removes brackets or parantheses and spaces
matrix2 = [list(map(float, t.split(","))) for t in inp2_strip.split(";")]  # creates a matrix for input


def row_times_column(row, col):  # don't need to check they are the right size here as it was already done
    result = 0
    length = len(row)  # you need to set a local variable for the length of a row/column
    for i in length:  # for each element in the row and column, you need to compute the product and add it to result
        for x in range(len(col)):
            result += row[i] * col[x]
    print('row times col result:', result)

    return result


def matrix_multiplication(mat1, mat2):
    Cols_2 = len(mat2[0])
    Cols_1 = len(mat1[0])  # number of rows and columns is needed
    Rows_2 = len(mat2)
    Rows_1 = len(mat1)
    product_matrix = [[0 for _ in range(Cols_2)] for _ in range(Rows_1)]
    if Rows_2 != Cols_1:  # if the product is not possible, return the correct message
        return "Undefined as the number of columns in the first matrix does not equal the number of rows in the second matrix."
    else:  # otherwise we want to calculate the product
       for i in range(Rows_1):
           for j in range(Cols_2):
               for k in range(Rows_2):
                   product_matrix.append(mat1[i][k] * mat2[k][j])
    return product_matrix


to_print = matrix_multiplication(matrix1, matrix2)

if type(to_print) == type(""):     #if the type is a string
    print(to_print)
else:    #Otherwise
    for r in to_print:
        print(r)
