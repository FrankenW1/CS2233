
def two_by_two_determinant(mat):
   val1 = mat[1][1] * mat[0][0]
   val2 = mat[0][1] * mat[1][0]
   det = val1 - val2
   return det

def eliminate_row_column(mat,k,l):
    new_matrix = [[t for t in row ] for row in mat]    #creates a new temp matrix that is equal to mat
    del new_matrix[k]# you need to eliminate a row and then eliminate the elements of a column (which can use a loop). You can use the pop() function here
    for item in range(len(new_matrix)):
        del new_matrix[item][l]
    return new_matrix

def determinant_calculator(mat):
    new_mat = []
    holder = []
    det = 0
    if len(mat) == 2:         #If the length of the input is 2, then we need to calculate the two_by_two determinant and return it
        det = two_by_two_determinant(mat)
    for i in range(len(mat)):          #We will fix and row or column and work through all of the entries, this will iterate through the elements in the row or column
        newmat = eliminate_row_column(mat, i, 0)      #We will need to eliminate the row and column
        sign = (-1) ** (i + 2)                       #We need to set the sign as (-1) ** (row + column)
        det2 = determinant_calculator(newmat)
        det += sign * mat[i][0] * det2
                     #We need to calculate the subdeterminant and then add the sign times the entry times the submatrix to the determinant

    return det

if __name__ == "__main__":
    inp = input()  # reads in the matrix
    inp_strip = inp.strip("(),[] ")  # removes brackets or parantheses and spaces
    matrix = [list(map(float, t.split(","))) for t in inp_strip.split(";")]  # creates a matrix for input

    if len(matrix) != len(matrix[0]):       # you will need an if statement to check that the matrix is square, if the size is 1, 2, 3, or something else. Each if statement will print a different result.
        print("Please enter a square matrix.")
    elif len(matrix) == 1:
        print(matrix[0][0])
    elif len(matrix) == 2:
        print(two_by_two_determinant(matrix))
    elif len(matrix) > 2:
        print(determinant_calculator(matrix))

