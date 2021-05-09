
def under_nonzero_finder(mat, m, k):  # find the first nonzero entry in a column after the kth entry. Need to read in the matrix and desired row because we read the matrix as a list of rows
    first_nonzero_loc = R + 1  # if all elements under the starting location are zero, it will return R+1
    for n in range(k, R):  # we need to work down our column starting at the kth element and then go through each row
        if mat[n][m] != 0:  # we want to check if the n,m entry is not zero
            first_nonzero_loc = n
              # if the element is not zero, we set the value to that location, n
            break
    return first_nonzero_loc


def subtract_row_times_num_to_row(first_row, sec_row, a):  # add a multiple of a row to another row
    for k in range(C):  # needs to iterate through each element in the row plus the augmented, so through the columns +1. This is accessed by a for loop of k in range(C+1)
        sec_row[k] = sec_row[k] - (a * first_row[k])

        '''Your code goes here'''  # we want to take the kth element of secrow, accessed through sec_row[k], and set it equal to itself minus a*(kth value of first_row)
    return sec_row


def echelon_calculator(mat):  # calculates the echelon form of a matrix
    i = 0
    j = 0
    counter = 0
    while j < C:

        zero_location = under_nonzero_finder(mat, j, i)

        zero_location = int(zero_location)
        if zero_location == R + 1:  # no pivot in the column
            j += 1  # move to the next column by adding one to j ****
        elif zero_location > i:  # the pivot is to low in the column
            temp_row = mat[zero_location]  # we need to switch rows. Store the pivot row temporarily
            counter += 1
            mat[zero_location] = mat[i]

            # move the ith row into the pivot location
            mat[i] = temp_row  # move the pivot into the correct spot

        else:
            for l in range(i + 1, R):
                a = mat[l][j] / mat[i][j]
                '''Your code goes here'''  # set a equal to the l,j element of mat divided by the i,j element
                mat[l] = subtract_row_times_num_to_row(mat[i], mat[l], a)

            j += 1
            i += 1

    return mat

     #You need to copy in your Echelon Calculator, but modify it to keep track of the number of row switches.
                              #The echelon calculator will need to return the matrix in echelon form and the number of switches.

def determinant_calculator_echelon(mat):
    det = 1
    nm = echelon_calculator(mat)     #this needs to turn the matrix into reduced echelon form and then use it to calculate the matrix
    for i in range(len(nm)):
        det *= nm[i][i]
    if det == -0.0:     #to fix the strange -0.0 case that happens in the echelon form calculator. You can also fix this in the echelon calculator
        det = 0.0
    return det

if __name__ == "__main__":
    inp = input()  # reads in the matrix
    inp_strip = inp.strip("(),[] ")  # removes brackets or parantheses and spaces
    matrix = [list(map(float, t.split(","))) for t in inp_strip.split(";")]  # creates a matrix for input
    R = len(matrix)  # number of rows
    C = len(matrix[0])  # number of columns

    if len(matrix) == len(matrix[0]):
        print(determinant_calculator_echelon(matrix))
    else:
        print('Please enter a square matrix.')
    '''Your Code Goes Here'''       #enter the correct print statements.
