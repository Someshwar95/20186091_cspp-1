def empty_tic_tac_toe():
	matrix = []
	for i in range(3):
		list_emp = input().split()
		matrix.append(list_emp)
	return matrix
def valid_input(tic_tac_toe):
	if sum(i.count('x') for i in tic_tac_toe) > 5 or sum(i.count('o') for i in tic_tac_toe) > 5:
		return "invalid game"
	for i in range(len(empty_tic_tac_toe)):
		for j in tic_tac_toe[i]:
			if j not in 'xo.':
				return "invalid input"
	return True
def winner_of_tic_tac_toe(tic_tac_toe):
	x = sum(i.count('x') for i in tic_tac_toe)
	o = sum(i.count('o') for i in tic_tac_toe)
	if x + o == 9:
		return "draw"
	elif x == 3:
		return "x"
	elif o == 3:
		return "o"
	elif x == 3 and o == 3:
		return "invalid game"
	elif tic_tac_toe[0][0] == tic_tac_toe[1][1] == tic_tac_toe[2][2]:
		return tic_tac_toe[0][0]
	elif tic_tac_toe[0][2] == tic_tac_toe[1][1] == tic_tac_toe[2][0]:
		return tic_tac_toe[0][2]

def main():
	matrix = empty_tic_tac_toe()
	matrix.valid_input(tic_tac_toe)
	matrixo = winner_of_tic_tac_toe(tic_tac_toe)

if __name__ == '__main__':
    main()
