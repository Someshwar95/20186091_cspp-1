def function(grid, i, j):
	inp = int(input())
	for x in range(i, 9):
		for y in range(j, 9):
			if grid[x][y] == 0:
				return x,y