inp = input()  # reads in the matrix
inp_strip = inp.strip("(),[] ")  # removes brackets or parantheses and spaces
matrix = [list(map(float, t.split(","))) for t in inp_strip.split(";")]  # creates a matrix for input

R = len(matrix)  # number of rows
C = len(matrix[0])  # number of columns

inpvec = input()  # reads in the column vector
vector = [float(t.strip("[](); ")) for t in inpvec.split(";")]  # creates a list for the b vector

for m in range(R):
    matrix[m] = matrix[m] + [vector[m]]  # extends the matrix

def under_nonzero_finder(mat, m, k):  # find the first nonzero entry in a column after the kth entry. Need to read in the matrix and desired row because we read the matrix as a list of rows
    first_nonzero_loc = R + 1  # if all elements under the starting location are zero, it will return R+1
    for n in range(k, R):  # we need to work down our column starting at the kth element and then go through each row
        if mat[n][m] != 0:  # we want to check if the n,m entry is not zero
            first_nonzero_loc = n
            # if the element is not zero, we set the value to that location, n
            break
    return first_nonzero_loc


def subtract_row_times_num_to_row(first_row, sec_row, a):  # add a multiple of a row to another row
   for k in range(C + 1):
    sec_row[k] = sec_row[k] - (a * first_row[k])  # we want to take the kth element of secrow, accessed through sec_row[k], and set it equal to itself minus a*(kth value of first_row)
    return sec_row


def mult_row_by_num(row, a):  # multiple a row by a constant
    for i in range(C + 1):  # needs to iterate through each element in the augmented row, so a for loop through the columns+1
        row[i] *= a  # needs to set the kth element equal to a*(kth element of the row)
    # print(row)
    return row


def echelon_calculator(mat):  # calculates the echelon form of a matrix
    i = 0
    j = 0
    while j < C:
        zero_location = under_nonzero_finder(mat, j, i)
        zero_location = int(zero_location)

        if zero_location == R + 1:  # no pivot in the column
            j += 1  # move to the next column by adding one to j
        elif zero_location > i:  # the pivot is to low in the column
            temp_row = mat[zero_location]  # we need to switch rows. Store the pivot row temporarily
            mat[zero_location] = mat[i]  # move the ith row into the pivot location
            mat[i] = temp_row  # move the pivot into the correct spot
        else:
            g = (1 / mat[i][j])
            mat[i] = mult_row_by_num(mat[i], g)  # set the leading element to 1 by setting the ith row =multi_row_by_num of the ith row times 1/ the i,j element
            for x in range(i + 1, R):  # clear out the value above the i,j element. Hint: very similar to the next for loop!
                mat[i][x] = 0
            for l in range(i + 1, R):
                a = mat[l][j] / mat[i][j]
                '''Your code goes here'''  # set a equal to the l,j element since i,j element is 1
                mat[l] = subtract_row_times_num_to_row(mat[i], mat[l], a)
            j += 1
            i += 1
    return mat


print(echelon_calculator(matrix))
