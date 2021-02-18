inp = input()
inp_strip = inp.strip("(),[] ")  # removes the parentheses or brackets and any spaces
matrix = [list(map(float, t.split(","))) for t in inp_strip.split(";")]  # creates a matrix for input

R = len(matrix)  # number of rows
C = len(matrix[0])  # number of columns


def zeros_under(mat, n, m):  # this will verify that all elements under the leading element in the n,m spot are zero
    check = True
    i = 0
    for i in range(n+1,R):     #this iterates from n+1 to R-1
        '''Your code goes here'''     #This checks along the mth column to make sure that elements under it are zero. You will want to use an if statement
        '''Your code goes here'''     #You want check to be false if you encounter a nonzero number
    return check


zeros_under(matrix, 0, 1)
