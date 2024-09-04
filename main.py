import numpy as np

# A random solvable Sudoku
gridSudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0], # 0
              [6, 0, 0, 1, 9, 5, 0, 0, 0], # 1
              [0, 9, 8, 0, 0, 0, 0, 6, 0], # 2
              [8, 0, 0, 0, 6, 0, 0, 0, 3], # 3
              [4, 0, 0, 8, 0, 3, 0, 0, 1], # 4
              [7, 0, 0, 0, 2, 0, 0, 0, 6], # 5
              [0, 6, 0, 0, 0, 0, 2, 8, 0], # 6
              [0, 0, 0, 4, 1, 9, 0, 0, 5], # 7
              [0, 0, 0, 0, 8, 0, 0, 7, 9]] # 8
            #  0  1  2  3  4  5  6  7  8

# gridSudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
#               [0, 0, 0, 0, 0, 0, 0, 0, 0], # 1
#               [0, 0, 0, 0, 0, 0, 0, 0, 0], # 2
#               [0, 0, 0, 0, 0, 0, 0, 0, 0], # 3
#               [0, 0, 0, 0, 0, 0, 0, 0, 0], # 4
#               [0, 0, 0, 0, 0, 0, 0, 0, 0], # 5
#               [0, 0, 0, 0, 0, 0, 0, 0, 0], # 6
#               [0, 0, 0, 0, 0, 0, 0, 0, 0], # 7
#               [0, 0, 0, 0, 0, 0, 0, 0, 0]] # 8
#             #  0  1  2  3  4  5  6  7  8

def printGrid(grid):
    """
    Prints the sudoku grid prettier
    """
    for row in range(len(grid)):
        if row % 3 == 0 and row != 0:
            print('- - - - - - - - - - -')
        for col in range(len(grid[0])):
            if col != len(grid[0])-1:
                if col % 3 == 0 and col != 0:
                    print("|", end=" ")
                print(grid[row][col], end=" ")
            else: print(grid[row][col])

def checkAvailable(grid, rowPos, colPos, n):
    """
    Checks if there's the same number in row or column
    """
    if n in grid[rowPos]:
        return False
    for row in grid:
        if n == row[colPos]:
            return False

    for row in range(rowPos//3 * 3, rowPos//3 * 3 + 3):
        for col in range(colPos//3 * 3, colPos//3 * 3 + 3):
            if grid[row][col] == n:
                return False

    return True

def notBlocked(grid):
    notBlockedSpaces = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                notBlockedSpaces.append([row, col])
    return notBlockedSpaces

notBlockedSpaces = notBlocked(gridSudoku)

def backTracking(grid, emptySpaces):
    number = 1
    position = 0
    isPossible = True
    iteration = 0

    # Enquanto a posição na lista de espaços vazios não for maior que a quantidade de espaços vazios
    while position < len(emptySpaces):
        # Enquanto o número não é possível, aumente o número em 1 e tente novamente
        while checkAvailable(grid, emptySpaces[position][0], emptySpaces[position][1], number) == False:
            number+=1

            # Caso nenhum número funcione, pare o loop
            if number > 9:
                isPossible = False
                break

        # Caso nenhum número funcione, resete a casa, volte à casa anterior e siga a partir do número dela
        if isPossible == False:
            number = grid[emptySpaces[position-1][0]][emptySpaces[position-1][1]]
            grid[emptySpaces[position][0]][emptySpaces[position][1]] = 0
            position-=1
            isPossible = True

        # Caso algum número funcione, siga para a próxima casa
        elif isPossible == True:
            grid[emptySpaces[position][0]][emptySpaces[position][1]] = number
            number = 1
            position+=1

        # Conta quantas iterações foram necessárias
        iteration+=1

        # Caso não haja possibilidade de resolver, imprime uma mensagem
        if position < 0:
            print('There are no valid solutions!')
            break

    print(f'It took {iteration} iterations to complete.')
    return grid

# printGrid(gridSudoku)
printGrid(backTracking(gridSudoku,notBlockedSpaces))
