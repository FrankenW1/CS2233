def two_by_two_determinant(mat):   #calculates the determinant of a two by two matrix
   val1 = mat[1][1] * mat[0][0]
   val2 = mat[0][1] * mat[1][0]
   det = val1 - val2
   return det

def eliminate_row_column(mat,k,l): # k = row, l = column
    new_matrix = [[t for t in row ] for row in mat]    #creates a new temp matrix that is equal to mat
    del new_matrix[k]# you need to eliminate a row and then eliminate the elemen                           ts of a column (which can use a loop). You can use the pop() function here
    for item in range(len(new_matrix)):
        del new_matrix[item][l]
    return new_matrix

def three_by_three_determinant(mat):
    part1 = eliminate_row_column(mat, 0, 0)
    part2 = eliminate_row_column(mat, 0, 1)
    part3 = eliminate_row_column(mat,0,2)
    val1 = two_by_two_determinant(part1)
    val2 = two_by_two_determinant(part2)
    val3 = two_by_two_determinant(part3)

    total = val1 - val2 + val3
    return total  # calculates a three by three by using two_by_two_determinant and eliminate_row_column

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
    elif len(matrix) == 3:
        print(three_by_three_determinant(matrix))
    else:
        print("We can only handle up to a 3 by 3 matrix. Sorry.")
