import functions as ft

def invert(M):
    #find the size of teh matrix
    num_rows, num_columns = len(M), len(M[0])
    #Make sure its square and has none zero determinant so that the inverse certainly exists.
    if (num_rows != num_rows) or (ft.determinant(M) == 0):
        raise Exception("Inverse doesn't exist")

    #Initialise the identity
    Id = [[0] * num_rows for _ in range(num_columns)]
    for i in range(num_rows):
        Id[i][i] = 1
    

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
        ft.row_swap(M, i, place_row_index)
        ft.row_swap(Id, i, place_row_index)
        #we then find the index of our next row
        place_row_index -= 1

    #Put in echelon form
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
                        ft.row_addition(M, changed_element_row, pivot_row, multiplier)
                        ft.row_addition(Id, changed_element_row, pivot_row, multiplier)

    #We put it into reduced row form by normalisin the pivots
    #we iterate through all the rows
    for pivot_row in range(num_rows):
        #iterate through the row until we find the pivot
        for pivot_column in range(num_columns):
            #check if we have the pivot
            if M[pivot_row][pivot_column] != 0:
                #we find out what we need to multiply the row by.
                multiplier = 1/M[pivot_row][pivot_column]
                ft.row_multiplication(M, pivot_row, multiplier)
                ft.row_multiplication(Id, pivot_row, multiplier)

    return Id













    return id
