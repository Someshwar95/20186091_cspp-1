def empty_tic_tac_toe():
    '''
    creating empty list for tic tac toe and appending input
    '''
    matrix = []
    for i in range(3):
        list_emp = input().split()
        matrix.append(list_emp)
    return matrix
def valid_input(tic_tac_toe):
    '''
    checking the input is valid or not
    '''
    if sum(i.count('x') for i in tic_tac_toe) > 5 or sum(i.count('o') for i in tic_tac_toe) > 5 or \
    (sum(i.count('o') for i in tic_tac_toe) == sum(i.count('x') for i in tic_tac_toe)):
        print("invalid game")
        return False
    for i in range(len(tic_tac_toe)):
        for j in tic_tac_toe[i]:
            if j not in 'xo.':
                print("invalid input")
                return False
    return True
def winner_of_tic_tac_toe(tic_tac_toe):
    '''
    checking for the winner of the game
    '''
    x_co = sum(i.count('x') for i in tic_tac_toe)
    o_co = sum(i.count('o') for i in tic_tac_toe)
    if x_co + o_co == 9:
        return "draw"
    elif x_co == 3:
        return "x"
    elif o_co == 3:
        return "o"
    elif x_co == 3 and o_co == 3:
        return "invalid game"
    elif tic_tac_toe[0][0] == tic_tac_toe[1][1] == tic_tac_toe[2][2]:
        return tic_tac_toe[0][0]
    elif tic_tac_toe[0][2] == tic_tac_toe[1][1] == tic_tac_toe[2][0]:
        return tic_tac_toe[0][2]

def main():
    '''
    calling the functions
    '''
    matrix = empty_tic_tac_toe()
    if valid_input(matrix):
        print(winner_of_tic_tac_toe(matrix))

if __name__ == '__main__':
    main()
