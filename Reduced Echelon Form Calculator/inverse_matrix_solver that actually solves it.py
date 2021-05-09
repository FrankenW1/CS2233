inp = input()  # reads in the matrix
inp_strip = inp.strip("(),[] ")  # removes brackets or parantheses and spaces
matrix = [list(map(float, t.split(","))) for t in inp_strip.split(";")]  # creates a matrix for input

R = len(matrix)  # number of rows
C = len(matrix[0])  # number of columns

inp2 = input()  # reads in the second matrix
inp2_strip = inp2.strip("(),[] ")  # removes brackets or parantheses and spaces

# use the next line if you want to call all of the matrix multiplication program
vector = [list(map(float, t.split(","))) for t in inp2_strip.split(
    ";")]  # creates a matrix for input vector. This is to use matrix multiplication below. This is unnecessary if you only call row_times_column and loop through the vector


# use the next line if you only want to use the row_times_column function
# vector = [float(t.strip("[](); ")) for t in inpvec.split(";")]    #creates a list for the b vector

def make_extended_matrix(mat):
    R = len(mat)  # number of rows
    C = len(mat[0])  # number of columns
    for m in range(
            R):  # we need to go to each row and then through each column. If we are on the diagonal, we add a 1.0 to the row. Otherwise we add a 0.0
        for x in range(C):
            if m == x:
                mat[m] = mat[m] + [1.0]
            else:
                mat[m] = mat[m] + [0.0]
    return mat


def under_nonzero_finder(mat, m,
                         k):  # find the first nonzero entry in a column after the kth entry. Need to read in the matrix and desired row because we read the matrix as a list of rows
    first_nonzero_loc = R + 1  # if all elements under the starting location are zero, it will return R+1
    # print(mat, m, k)
    for n in range(k, R):  # we need to work down our column starting at the kth element and then go through each row
        if mat[n][m] != 0:  # we want to check if the n,m entry is not zero
            first_nonzero_loc = n
            # if the element is not zero, we set the value to that location, n
            break

    return first_nonzero_loc


def subtract_row_times_num_to_row(first_row, sec_row, a):  # add a multiple of a row to another row
    for k in range(len(first_row)):
        sec_row[k] = sec_row[k] - (a * first_row[
            k])  # we want to take the kth element of secrow, accessed through sec_row[k], and set it equal to itself minus a*(kth value of first_row)
    return sec_row


def mult_row_by_num(row, a):  # multiple a row by a constant
    for i in range(len(
            row)):  # needs to iterate through each element in the augmented row, so a for loop through the columns+1
        row[i] *= a  # needs to set the kth element equal to a*(kth element of the row)
    # print('row', row)
    # print('a', a)
    return row


def reduced_echelon_calculator(mat):  # calculates the echelon form of a matrix
    i = 0
    j = 0
    while j < C:
        zero_location = under_nonzero_finder(mat, j, i)
        zero_location = int(zero_location)
        if zero_location == R + 1:  # no pivot in the column
            j += 1  # move to the next column by adding one to j ****
        elif zero_location > i:  # the pivot is to low in the column
            temp_row = mat[zero_location]  # we need to switch rows. Store the pivot row temporarily
            mat[zero_location] = mat[i]

            # move the ith row into the pivot location
            mat[i] = temp_row  # move the pivot into the correct spot

        else:
            g = (1 / mat[i][j])
            mat[i] = mult_row_by_num(mat[i],
                                     g)  # set the leading element to 1 by setting the ith row =multi_row_by_num of the ith row times 1/ the i,j element
            for k in range(i):
                x = mat[k][j]
                mat[k] = subtract_row_times_num_to_row(mat[i], mat[k], x)

            for l in range(i + 1, R):
                a = mat[l][j] / mat[i][j]
                '''Your code goes here'''  # set a equal to the l,j element of mat divided by the i,j element
                mat[l] = subtract_row_times_num_to_row(mat[i], mat[l], a)
            j += 1
            i += 1
    # print('matz', mat)
    return mat

    # FIX THIS RIGHT HERE
    # You need to insert the code for the reduced echelon calculator, but you need to modify it to define the length of the inputs locally.
    # For instance, mult_row_by_num(row,a) can use len(row) to determine the value used in the for loop range


def inverse_calculator(mat):
    C = len(mat[0])
    R = len(mat)
    if C != R:  # this is the case where the matrix is not square
        return 'There is no inverse matrix as this matrix is not square.'
    else:
        make_extended_matrix(mat)  # use make_extended_matrix to create the augmented matrix
        # print(mat)
        reduced_extended_matrix = reduced_echelon_calculator(
            mat)  # do the matrix reduction to produce a reduced row echelon on one side and the potential inverse of the other
        # print('rem', reduced_extended_matrix)
        if mat[R - 1][
            C - 1] != 1:  # This is the case where the matrix is square but not invertible. Hint: If the last column of the left side matrix does not have a one (it would be zero) at the bottom, there is a free variable and the matrix is not invertible
            return 'The matrix is square but it is not invertible.'
        else:  # Otherwise we continue
            inverse = [[0 for _ in range(C)] for _ in range(R)]  # creates matrix of the correct size
            for i in range(R):  # IT HAS TO DO WITH THIS <- THE I IN RANGE BLAH BlAH IS THE BUG
                for j in range(C, C * 2,
                               1):  # we need a double for loop to run through right side of the augmented matrix
                    inverse[i][j - C] = reduced_extended_matrix[i][j]
    return inverse
    # You need to put all of the inverse matrix calculator code in here. This includes the function needed to extend the matrix


def row_times_column(row, col):  # don't need to check they are the right size here as it was already done
    result = 0
    length = len(row)  # you need to set a local variable for the length of a row/column
    for i in length:  # for each element in the row and column, you need to compute the product and add it to result
        for x in range(len(col)):
            result += row[i] * col[x]
    print('row times col result:', result)

    return result


def matrix_multiplication(mat1, mat2):
    Rows_1 = len(mat1)
    Cols_1 = len(mat1[0])
    Rows_2 = len(mat2)
    Cols_2 = len(mat2[0])

    product_matrix = [[0 for _ in range(Cols_2)] for _ in range(Rows_1)]
    if Cols_1 != Rows_2:  # if the product is not possible, return the correct message
        return "Undefined as the number of columns in the first matrix does not equal the number of rows in the second matrix."
    else:  # otherwise we want to calculate the product
        # iterate through rows of X
        for i in range(Rows_1):  # iterate through columns of Y
            for j in range(Cols_2):  # iterate through rows of Y
                for k in range(Rows_2):
                    product_matrix[i][j] += mat1[i][k] * mat2[k][j]
        return product_matrix

    # You need to put all or part of the matrix multiplication code in here. Your choice here will decide what your solver function looks like


def inverse_times_vector(mat,
                         vector):  # define a function that takes in a matrix and vector and calculates the inverse times the vector
    R = len(mat)
    C = len(mat[0])
    if R != C or len(vector) != R:  # If the matrix is not square, set solution as the correct string.
        return "The system is not solvable as the matrix and vector are not the right size."
    else:  # Otherwise calculate the inverse
        inverse = inverse_calculator(mat)
        if type(inverse) == str:
            solution = inverse  # this will return the correct message if the coefficient matrix is not invertible
        else:  # Otherwise we need to calculate the product of the inverse matrix and the column vector
            solution = matrix_multiplication(inverse, vector)
    return solution  # return your answer, called solution


to_print = inverse_times_vector(matrix,
                                vector)  # call the function with matrix and vector as the inputs and assign it to the variable to_print

if type(to_print) == str:
    print(to_print)
else:
    z = 0
    for r in to_print:  # otherwise we need to interate through the list and print each value using the required format
        z += 1
        print("x_{} = {:0.3f}".format(z,r[0]))
