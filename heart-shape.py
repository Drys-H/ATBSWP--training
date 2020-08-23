#! python 3

# heart-shape.py - turn the heart shape to stand on it point 


grid = [['.', '.', '.', '.', '.', '.',],
        ['.', 'O', 'O', '.', '.', '.',],
        ['O', 'O', 'O', 'O', '.', '.',],
        ['O', 'O', 'O', 'O', 'O', '.',],
        ['.', 'O', 'O', 'O', 'O', 'O',],
        ['O', 'O', 'O', 'O', 'O', '.',],
        ['O', 'O', 'O', 'O', '.', '.',],
        ['.', 'O', 'O', '.', '.', '.',],
        ['.', '.', '.', '.', '.', '.',]]


x = 0
y = 0

while x < len(grid[0]):               #Determine number of lists in list
    while y < len(grid):              #Determine number of lists
        print(grid[y][x], end='')     #Print each element on line
        y += 1                        #Up Y by one each cycle until while stops
    print('\n')                       #Move to a new line
    x += 1                            #Increase x by one and reset Y, restarts 
    y = 0
       


