import functions as pr

#Didn't bother to comment so rigerously for this part as its not relevant to the question

def main():
    #we introduce the program and tell the user what it can do
    print("Welcome to our project. The following options are available in finding the dimension of a spanning set")
    print(" 1 - Elementary row operatios")
    print(" 2 - Matrix products")
    print(" 3 - Row Reduction")
    print(" 4 - Step by step row reduction")
    print(" 5 - Finding the a basis of a spanning set")
    print(" 6 - Finding  the dimension of a spanning set by eschelon form")
    print(" 7 - Finding  the dimension of a spanning set by minor method")
    print(" 8 - Exit")
    #initialise our check if a valid input is given
    selection = None
    #check if the input is valid and taking an input for which functionality should be used
    while selection not in [1,2,3,4,5,6,7]:
        selection = int(input("Choose an options from above, inputting your answer as an integer: "))
    if selection == 1:
        print("Select an elementary row operation")
        print(" 1 - Swap")
        print(" 2 - Row addition")
        print(" 3 - Scalar row multiplication")
        selection = None
        while selection not in [1,2,3]:
            selection = int(input("Choose an options from above, inputting your answer as an integar: "))
        if selection == 1:
            print("Input a matrix")
            M = pr.input_matrices()
            p, q = None, None
            while (p not in range(len(M)+1)) and (q not in range(len(M)+1)):
                p = int(input("Which row would you like to swap: "))-1
                q = int(input("What would you like to swap it with: "))-1
            pr.print_matrix(pr.row_swap(M, p, q))
        elif selection == 2:
            print("Input a matrix")
            M = pr.input_matrices()
            p, q, multiple = None, None, None
            while (p not in range(len(M)+1)) and (p not in range(len(M)+1)) and (multiple != float):
                p = int(input("Which row would you like to add too: "))-1
                q = int(input("which row would you like to add: "))-1
                multiple = float(input("What would you like to multiply row " + q + " with before adding: "))
            pr.print_matrix(pr.row_addition(M, p, q, multiple))
        else:
            print("Input a matrix")
            M = pr.input_matrices()
            row = None
            multiple = None
            while (row not in range(len(M)+1) ) and (type(multiple) != float):
                row = input("Which row would you like to multiply: ")-1
                multiple = input("Which scalar would you like to  multiply by: ")
            pr.print_matrix(pr.row_multiplication(M, row, multiple))

    elif selection == 6:
        print("Input your vectors")
        M = pr.input_vectors()
        dim = pr.Dimension(M)
        print("The dimension of the space spanned by these vectors is " + str(dim) +".")
        selection = input("Would you like to know a basis as well (y/n): ")
        if selection == "y":
            basis = pr.span_basis(M)
            pr.print_matrix(basis)
    elif selection == 5:
        print("Input your vectors")
        M = pr.input_vectors()
        basis = pr.span_basis(M)
        print("A basis of the space spanned by these vectors is :")
        pr.print_matrix(basis)
    elif selection == 7:
        print("Input your vectors")
        M = pr.input_vectors()
        dim = pr.minor(M)
        print("The dimension of the space spanned by these vectors is " + str(dim) +".")
    elif selection == 2:
        print("Input the left hand matrix")
        left_matrix = pr.input_matrices()
        print("Input the right hadn side matrix")
        right_matrix = pr.input_matrices()
        product = pr.matrix_product(left_matrix, right_matrix)
        print("The product is: ")
        pr.print_matrix(product)
    elif selection == 3:
        print("Input your Matrix")
        matrix = pr.input_matrices()
        rref = reduced_row_eschelon(matrix)
        print("The reduced row eschelon form of the matrix is")
        pr.print_matrix(rref)
    elif selection == 4:
        print("Input a matrix")
        matrix = pr.input_matrices()
        print("First we put all the zero rows at the bottom of the matrix:")
        matrix = pr.organise_zero_rows(matrix)
        pr.print_matrix(matrix)
        print("Then we order the pivots from highest to lowest:")
        matrix = organise_pivots(M)
        pr.print_matrix(matrix)
        print("We then put it into row eschelon form by subtracting the rows fromm eachother: ")
        matrix = row_eschelon(matrix)
        pr.print_matrix(matrix)
        print("Finally. we divide all the pivots by themselves to make sure they're all equal to 1: ")
        matrix = pr.pivot_normalisation(matrix)
        pr.print_matrix(matrix)
        print("After find this we can then remove all the zero rows: ")
        matrix = pr.eliminate_zero_rows(matrix)
        pr.print_matrix(matrix)
        print("And count the remaining row to find the dimension is the row space is" + str(len(matrix)))
    else:
        exit()










        
