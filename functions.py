#import numpy as np



#Debug example matrices
M1 = [[2,3],[4,5]]
M2 = [[0,0],[1,0]]
M3 = [[0,0],[0,2],[0,1],[1,1]]
M4 = [[0,1, 1], [0,0, 2], [0,0, 1], [0,0, 0]]
M5 = [[1,2],[2,4]]
M6 = [[1,2],[3,4],[5,6]]
M7 = [[1],[2]]
M8 = [[3,4]]
M9 = [[3,4],[5,6],[-6,-8]]
M10 = [[1,2,3],[4,5,6],[7,8,9]]
M11 = [[1,2,3],[2,4,7],[1,3,2]]

#We define a function to perform the swap elementry row opertation
def row_swap(M,p,q):
    #Determine the size of the matrix so we dont need to have extra arguments in teh function.
    n = len(M)
    m = len(M[0])
    #Create a variable to store the row which is going to be replaced
    temp = M[p]
    #replace the row p with row q
    M[p] = M[q]
    #replace row q with the copy of row p
    M[q] = temp
    return M

#We define a function to perform addition elementry row operation.
def row_addition(M, p, q, f):
    #Temporarily store the rows p and q for saftey
    tempq = M[q]
    tempp = M[p]
    #iterate through the row performing the operation to each of the elements in row p
    for i in range(len(tempp)):
        tempp[i] = tempp[i] + f* tempq[i]
    # return the temporary row variables in the matrix
    M[p] = tempp
    M[q] = tempq
    return M

#We define a function to perform scaler multiplication elementry row operation.
def row_multiplication(M, p, f):
    #Temporarily store row p for saftey
    temprow = M[p]
    #Iterate through row p multiplying each element by f
    for i in range(len(temprow)):
        temprow[i] = f*temprow[i]
    #return the temporary row into the matrix
    M[p] = temprow
    return M

#We define a function to put all teh zero rows at teh end of a matrix using row reduction.
def organise_zero_rows(M):
    #We determine the dimensions of M
    num_rows = len(M)
    num_columns = len(M[0])
    #Create a list of all the zero rows
    zero_rows = []
    #we then iterate through the rows to check fi they're zero rows.
    for i in range(num_rows):
        #create a boolean to see if this row is a zero row
        is_zero_row = True
        #iterate through each row check if each element in row i is 0.
        for j in range(num_columns):
            #check if the element is not zero
            if M[i][j] != 0:
                #if the element is not zero we know its not a zero row.
                is_zero_row = False
        #check if its definatly a zero row
        if is_zero_row == True :
            #if its a zero row add it to the list of zero rows
            zero_rows.append(i)
    #we find out how many zero rows we have so that we know where to put them
    num_zero_rows = len(zero_rows)
    #we find out where to put the first zero row
    place_row_index = num_rows - num_zero_rows
    #we then iterate through the zero rows putting them at the bottom of the matrix
    for i in zero_rows:
        #if its a zero row we swap it with one of the
        row_swap(M, i, place_row_index)
        #we then find the index of our next row
        place_row_index -= 1
    return M

#we define a function to put the largest pivot points at the top.
def organise_pivots(M):
    #We determine the dimensions of M
    num_rows = len(M)
    num_columns = len(M[0])
    #We then do a bubble sort cause its easiest to implement.
    #Create a boolean to check if its sorted.
    sorted_check = False
    #We repeat the bubble sort until the list is sorted
    while sorted_check == False:
        #set soted check to true until we find ut where its not sorted.
        sorted_check = True
        #We iterate through the columns to swap neighbours
        for i in range(num_rows - 1):
            # we find which of the ith and i+1th element is none zero and and laregst.
            for j in range(num_columns):
                #check if we need to swap them.
                if (M[i][j] < M[i+1][j]):
                    #if row i+1 is bigger than i the we swap so the biggest is on top with the smallest index
                    row_swap(M,i,i+1)
                    sorted_check = False
                #We then check if we've searched sufficiently through this row.
                if M[i][j] != 0 or M[i+1][j] != 0:
                    #we move onto the next bubble
                    break
    return M

#We next define a function to make all the elements below each pivot are zero.
def row_eschelon(M):
    #We determine the dimensions of M
    num_rows = len(M)
    num_columns = len(M[0])
    #We then iterate through each of the rows
    for pivot_row in range(num_rows):
        #for each row we iterate through to find the pivot
        for pivot_column in range(num_columns):
            if M[pivot_row][pivot_column] != 0:
                #we evaluate the pivot value and store it in a variable
                pivot_value = M[pivot_row][pivot_column]
                #we iterate though all the rows below doing additons until the elements are all zeros
                for changed_element_row in range(num_rows):
                    #we make sure not to subtract a row by itself
                    if changed_element_row != pivot_row:
                        multiplier = -M[changed_element_row][pivot_column]/pivot_value
                        row_addition(M, changed_element_row, pivot_row, multiplier)
                break
    return M

#We define a function to make all the pivots equal to 1
def pivot_normalisation(M):
    #We determine the dimensions of M
    num_rows = len(M)
    num_columns = len(M[0])
    #we iterate through all the rows
    for pivot_row in range(num_rows):
        #iterate through the row until we find the pivot
        for pivot_column in range(num_columns):
            #check if we have the pivot
            if M[pivot_row][pivot_column] != 0:
                #we find out what we need to multiply the row by.
                multiplier = 1/M[pivot_row][pivot_column]
                row_multiplication(M, pivot_row, multiplier)
                break
    return M

#we define a function to perform the entire gauss jordan operation from the function steps we've already defined
def reduced_row_eschelon(M):
    #We let M equal to its reduced form
    M = pivot_normalisation(row_eschelon(organise_pivots(organise_zero_rows(M))))
    return M
    
#we define a function to take the transverrse of a matrix
def transpose(M):
    #We determine the dimensions of M
    num_rows = len(M)
    num_columns = len(M[0])
    #we initialise a new natrix
    transpose = [[None] * num_rows for _ in range(num_columns)]
    #we iterate through the rows and columns of M
    for row in range(num_rows):
        for column in range(num_columns):
            #we add the element to transverse with opposite row and column indicies
            transpose[column][row] = M[row][column]
    return transpose

#we define a function to take the matrix product of two matrices
def matrix_product(N,M):
    #We find the dimensions of our output matrix and the number of terms in each sum
    num_rows = len(N)
    num_columns = len(M[0])
    num_terms = len(M)
    #initialise an ourput matrix
    T = [[None] * num_rows for _ in range(num_columns)]
    #iterate through evaluating the lements of T
    for row in range(num_rows):
        for column in range(num_columns):
            #we initialise a temporary variable to calculate the element
            temp_element = 0
            #We then iterate through all theh terms that make up the element in T
            for term_index in range(num_terms):
                #we add the term to our temporary element
                temp_element += M[term_index][column] * N[row][term_index]
            #pass the sum into the output matrix
            T[row][column] = temp_element
    return T

#we define a function to eliminate the zero row from a matrix
def eliminate_zero_rows(M):
    #we find the dimensions of the matrix
    num_rows = len(M)
    num_columns = len(M[0])
    #create a list to store all the none zero rows
    none_zero_rows = []
    #we iterate through all the rows
    for row in range(num_rows) :
        #we create a boolean to tell us if the row is a zero row
        is_zero_row = True
        #we iterate throught the elements until we find a none zero element
        for column in range(num_columns):
            if M[row][column] != 0:
                is_zero_row = False
        #if we dont find one we remove the vector from the list
        if is_zero_row == False:
            #store the idex of the zero row
            none_zero_rows.append(row)
    #Create a new list to add the none zero rows too
    N = []
    #iterate through all the none zero rows and append the none zero rows
    for row in none_zero_rows:
        N.append(M[row])
    return N

#We define a function to take in a list of spanning vectors and gives a basis.
def span_basis(M):
    #we find the number of vectors and the number of coordinates of the space
    num_vectors = len(M)
    num_coordinates = len(M[0])
    #we first turn the spanning basis into a matrix to find its kernel
    N = transpose(M)
    #We find the reduced row eschelon form of the matrix N
    rref = reduced_row_eschelon(N)
    #we then find a new basis set by multiplying the rref by the list of vectors (Justify this)
    B = matrix_product(rref,M)
    #we then remove all the zero vectors from the list
    B = eliminate_zero_rows(B)
    return B

#we define a function to determine the dimension of the basis
def Dimension(M):
    #find the transpose of the list of vectors
    M = transpose(M)
    #Row reduce the transpose
    M = reduced_row_eschelon(M)
    #eliminate the zero rows
    M = eliminate_zero_rows(M)
    #Count the number of none zero rows in M
    Dimension = len(M)
    return Dimension

#We define a function to allow users to imput matrices
def input_matrices():
    #check boolean to see if the user has input the correct matrix
    correct_input = False
    #check that the correct matrix is input
    while correct_input == False:
        #we initialise the columns and rows
        num_rows = None
        num_columns = None
        #We make sure the number of rows and columns are integars (figure out how to stop false inputs)
        while (type(num_rows) != int) and (type(num_columns) != int) :
            #We retreive the number of rows and columns
            num_rows = int(input("Number of rows: "))
            num_columns = int(input("Number of columns: "))
        #initialise the output matrix
        M = [[None] * num_rows for _ in range(num_columns)]
        #We iterate through the rows and columns of the matrix finding the 
        for row in range(num_rows):
            for column in range(num_columns):
                #receive the input for the element at this index, adding one to accound for indexing from 0
                M[row][column] = float(input("Element in row " + str(row+1) + " and column " + str(column+1) + ": "))
        #we then output the selected matrix
        print("You have selected the matrix:")
        #iterare through outputting each of the rows.
        for row in range(num_rows):
            print(M[row])
        #ask if the matrix is correct
        check_string = input("Is this matrix correct (y/n): ")
        #if it is correct set check string to true so we can move on to the output.
        if check_string == "y":
            correct_input = True
        else:
            correct_input = False
    return M

#we define a function to print a matrix
def print_matrix(M):
    #iterate through the length of the matrix printing each row
    for i in range(len(M)):
        print(M[i])

#we define a function to input a list of vectors
def input_vectors():
    #check boolean to see if the user has input the correct vectors
    correct_input = False
    #check that the correct vectors are input
    while correct_input == False:
        #we initialise the columns and rows of our list
        num_rows = None
        num_columns = None
        #We make sure the number of rows and columns are integars (figure out how to stop false inputs)
        while (type(num_rows) != int) and (type(num_columns) != int) :
            #We retreive the number of rows and columns
            num_rows = int(input("Number of vectors: "))
            num_columns = int(input("Number of coordinates: "))
            
        #initialise the output list
        M = [[None] * num_columns for _ in range( num_rows  )]
        #We iterate through the rows and columns of the list finding the 
        for column in range(num_columns):
            for row in range(num_rows):
                #receive the input for the element at this index, adding one to accound for indexing from 0
                M[row][column] = float(input("Vector " + str(column+1) +  ", element " + str(row+1) + ": "))

        #we then output the selected vectors
        print("You have selected the vectors:")
        #print the selected matrix
        print_matrix(M)
        #ask if the vectors are correct
        check_string = input("Are these vectors correct (y/n): ")
        #if it is correct set check string to true so we can move on to the output.
        if check_string == "y":
            correct_input = True
        else:
            correct_input = False
    return M

#We define a function to calculate the determinant
def determinant(M):
    #make sure its a square matrix
    if len(M) != len(M[0]):
        return None
    #Check if the determinant is 1 by 1
    if len(M) ==1 and len(M[0]) == 1:
        return M[0]
    #Calculate for a 2 by 2 case written explicitly
    if len(M) == 2 and len(M) == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]  
    #let determinant be o which we can then add too.
    det = 0
    #if the matrix is bigger than 2 by 2 we use the laplace method by iterating through the first row
    for c in range(len(M[0])):
        #find the submatrix, i think this is somtimes called a minor
        submatrix = [row[:c] + row[c+1:] for row in M[1:]]
        #add the value to the determinant
        det += M[0][c] * ((-1) ** c) * determinant(submatrix)
    return det

#we now define a function to find the rank of a matrix using the minor method.
def minor(M):
    #We first let the rank be equal to 0
    rank = 0
    #we then find the rows and columns of the matrix
    num_rows, num_columns = len(M), len(M[0])
    #We then iterate through the row by the minimum of the lengths and rows *
    for i in range(min(num_rows,num_columns)):
        rank_increase = False
        #and then find the determinant of the resulting sub matrices iterating through all the possible combinations
        for j in range(num_columns):
            #We find the submatrix *
            minor = [row[:j] + row[j+1:] for row in M[:i] + M[i+1:]]
            #then find the determinant of the minor matrix
            det = determinant(minor)
            #check if the matrix has all linearly independent rows
            if det != 0 :
                #this means the rank is increased
                rank_increase = True
                #we consider the next element in the column
                break
        if rank_increase == True:
            rank += 1
    return rank



##
###we define a function to allow for all the functionality of the program
##def main():
##    #we introduce the program and tell the user what it can do
##    print("Welcome to our project. the following options are available in finding the dimension of a spanning set")
##    print(" 1 - Elementary row operatios")
##    print(" 2 - Matrix products")
##    print(" 3 - Row Reduction")
##    print(" 4 - Step by step row reduction")
##    print(" 5 - Finding the a basis of a spanning set")
##    print(" 6 - Finding  the dimension of a spanning set")
##    print(" 7 - Exit")
##    #initialise our check if a valid input is given
##    selection = None
##    #check if the input is valid and taking an input for which functionality should be used
##    while selection not in [1,2,3,4,5,6,7]:
##        selection = int(input("Choose an options from above, inputting your answer as an integer: "))
##    if selection == 1:
##        print("Select an elementary row operation")
##        print(" 1 - Swap")
##        print(" 2 - Row addition")
##        print(" 3 - Scalar row multiplication")
##        selection = None
##        while selection not in [1,2,3]:
##            selection = int(input("Choose an options from above, inputting your answer as an integar: "))
##        if selection == 1:
##            print("Input a matrix")
##            M = input_matrices()
##            p, q = None, None
##            while (p not in range(len(M)+1)) and (q not in range(len(M)+1)):
##                p = int(input("Which row would you like to swap: "))-1
##                q = int(input("What would you like to swap it with: "))-1
##            print_matrix(row_swap(M, p, q))
##        elif selection == 2:
##            print("Input a matrix")
##            M = input_matrices()
##            p, q, multiple = None, None, None
##            while (p not in range(len(M)+1)) and (p not in range(len(M)+1)) and (multiple != float):
##                p = int(input("Which row would you like to add too: "))-1
##                q = int(input("which row would you like to add: "))-1
##                multiple = float(input("What would you like to multiply row " + q + " with before adding: "))
##            print_matrix(row_addition(M, p, q, multiple))
##        else:
##            print("Input a matrix")
##            M = input_matrices()
##            row = None
##            multiple = None
##            while (row not in range(len(M)+1) ) and (type(multiple) != float):
##                row = input("Which row would you like to multiply: ")-1
##                multiple = input("Which scalar would you like to  multiply by: ")
##            print_matrix(row_multiplication(M, row, multiple))
##
##    elif selection == 6:
##        print("Input your vectors")
##        M = input_vectors()
##        dim = Dimension(M)
##        print("The dimension of the space spanned by these vectors is " + str(dim) +".")
##        selection = input("Would you like to know a basis as well (y/n): ")
##        if selection == "y":
##            basis = span_basis(M)
##            print_matrix(basis)
##    elif selection == 5:
##        print("Input your vectors")
##        M = input_vectors()
##        basis = span_basis(M)
##        print("A basis of the space spanned by these vectors is :")
##        print_matrix(basis)

        







    
    
