'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
     # if sum(i.count('1') for i in sudoku) > 9 or sum(i.count('2') for i in sudoku) >
     # 9 or sum(i.count('3') for i in sudoku) > 9 or\
     # sum(i.count('4') for i in sudoku) > 9 or sum(i.count('5') for i in sudoku) >
     # 9 or sum(i.count('6') for i in sudoku) > 9 or\
     # sum(i.count('7') for i in sudoku) > 9 or sum(i.count('8') for i in sudoku) >
     # 9 or sum(i.count('9') for i in sudoku) > 9:
     #  (sum(i.count('o') for i in sudoku) == sum(i.count('x') for i in sudoku)):
     #    print("invalid game")
     #    return False
    for i in range(len(sudoku)):
        for j in sudoku[i]:
            if j not in '123456789':
                return False

    return True

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''

    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
