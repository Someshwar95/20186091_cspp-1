def mult_matrix(matrix1_var, matrix2_var):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    # rows = len(m1)
    # columns = len(m2[0])
    # multi_matrix = [[0 for i in range(columns)] for j in range(rows)]
    # pass
    add_ = re_mat(len(matrix1_var), len(matrix2_var[0]))
    if len(matrix1_var[0]) == len(matrix2_var):
        for row_ in range(len(matrix1_var)):
            for col_ in range(len(matrix2_var[0])):
                for com_ in range(len(matrix2_var)):
                    add_[row_][col_] += matrix1_var[row_][com_] * matrix2_var[com_][col_]
        return add_
    
    print("Error: Matrix shapes invalid for mult")
    return None

def add_matrix(matrix1_var, matrix2_var):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    add_ = re_mat(len(matrix1_var), len(matrix1_var[0]))
    if len(matrix1_var) == len(matrix2_var) and len(matrix1_var[0]) == len(matrix2_var[0]):
        for i in range(len(matrix1_var)):
            for j in range(len(matrix1_var[0])):
                add_[i][j] += (matrix1_var[i][j] + matrix2_var[i][j])
        return add_

    print("Error: Matrix shapes invalid for addition")
    return None
def re_mat(rows, columns):
    add_matrix = [[0 for i in range(columns)] for j in range(rows)]
    return add_matrix

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    list_input = input().split(',')
    rows, columns = int(list_input[0]), int(list_input[1])
    for _ in range(rows):
        list_matrix_row = input().split()
        if columns == len(list_matrix_row):
            matrix.append([int(i) for i in list_matrix_row])
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix

def main():
    # read matrix 1
    matrix_one = read_matrix()
    if matrix_one is None:
        exit()

     # read matrix 2
    matrix_two = read_matrix()
    if matrix_two is None:
        exit()

    # add matrix 1 and matrix 2

    print(add_matrix(matrix_one, matrix_two))

    # multiply matrix 1 and matrix 2

    print(mult_matrix(matrix_one, matrix_two))

if __name__ == '__main__':
    main()
