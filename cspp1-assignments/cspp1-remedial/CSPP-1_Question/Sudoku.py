def print_grid(arr): 
    for i in range(9): 
        for j in range(9): 
            print (arr[i][j])
            print ('Given sudoku is solved')
def find_empty_location(arr,l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False