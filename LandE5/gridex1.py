# Write your code here :-)
import time, copy

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]



for i in range(len(grid[0])): #length of the last element of the list(number of columns)
    for j in range(len(grid) - 1, -1, -1): #length of the whole list (number of rows) & steps to loop backwards
        #if j < 1: row ot if i < 1 col
        if j == 0:
            print(grid[j][i], end = '\n')

        else:
            print(grid[j][i], end = '')


'''small_grid = [[1, 4, 7],
              [2, 5, 8],
              [3, 6, 9],]

for i in range(len(small_grid)):
    for j in range(len(small_grid[i])):
        #if j < 1: row ot if i < 1 col
        if j == 2:
            print(small_grid[j][i], end = '\n')

        else:
            print(small_grid[j][i], end = '')


        #print(small_grid[j][i], end = ' ')'''



''''for x in grid:
    for y in x:
        print(y)'''










