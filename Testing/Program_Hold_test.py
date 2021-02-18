inp_strip = inp.strip("(),[] ")    #removes the parantheses or brackets and any spaces
matrix = [list(map(float, t.split(","))) for t in inp_strip.split(";")]    #creates a matrix for input

R = len(matrix)       #number of rows
C = '''Your Code Here'''    #number of columns

def zeros_under(mat,n,m):     #this will verify that all elements under the leading element in the n,m spot are zero
    check = True
    i = 0
    for i in range(n+1,R):     #this iterates from n+1 to R-1
        '''Your code goes here'''     #This checks along the mth column to make sure that elements under it are zero. You will want to use an if statement
        '''Your code goes here'''     #You want check to be false if you encounter a nonzero number
    return check

def zeros_above(mat,n,m):     #this will verify that all elements above the leading element in the n,m spot are zero
    check = True
    i = 0
    '''Your codes goes here'''      #Hint: This is very similar to zeros_under but you need to iterate from 0 to n-1. Be sure to return the value of check

def echelon_checker(mat):    #checks if the matrix is in echelon form
    i = 0
    j = 0
    echelon = True
    while echelon == True and i <R and j<C:         #iterates through locations in the matrix
        echelon = zeros_under(mat,i,j)              #checks if the column satisfies echelon conditions
        if mat[i][j] == 0:                          #if it is a zero entry, we need to move to the next column
            j +=1
        else:                                       #move down a row and column to continue
            i +=1
            j +=1
    return echelon

def reduced_echelon_checker(mat):                   #checks if the matrix is in reduced echelon form
    i = 0
    j = 0
    reduced_echelon = True
    while '''Your code goes here''':     #iterates through locations in the matrix
        if '''Your code goes here''':    #if it is a zero entry, we check that it zeros under it and we need to move to the next column
            '''Your code goes here'''
            '''Your code goes here'''
        elif mat[i][j] == 1:        #if it is not zero we check that it is a 1 and that is in reduced echelon form. Then we move over and down one
            '''Your code goes here''' and '''Your code goes here'''
            i += 1
            j += 1
        '''Your code goes here'''
            '''Your code goes here'''                      #this means that we have a leading entry that is not a one. So the value needs to be false
    return reduced_echelon



if echelon_checker(matrix) == True:
    print("The matrix is in echelon form.")
else:
    print("The matrix is not in echelon form.")

'''Your code goes here'''                    #Return the correct statements for reduced_echelon_checker
