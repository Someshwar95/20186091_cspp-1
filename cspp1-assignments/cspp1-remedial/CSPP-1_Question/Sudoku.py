def sudoku(sudoku):
    for j in range(len(sudoku)):
        for i in range(len(sudoku)):
            if sudoku[j][i] not in '123456789' or len(set(sudoku[j])) != 9:
                return 'False'
    for k in zip(*sudoku):
        for l in list(k):
            if l not in '123456789' or len(set(list(k))) != 9:
                return 'False'
    return 'True'