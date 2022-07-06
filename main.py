import numpy as np
import pygame
import time
#scan N from user
N=int(input('Enter Number of N Queens \n'))

#pygame initialization
pygame.init()
#display frame 600 x 600
win = pygame.display.set_mode((800,800))
#display queen(50 x50)
queen= pygame.transform.scale(pygame.image.load('queen.jpg'),(50,50))


# draw NQueen
def draw(board):

    win = pygame.display.set_mode((800,800))

    win.fill((255,255,255))
    #A=[]
    for i in range(N):
        for j in range(N):
            if board[j][i]==0:
                pygame.draw.rect(win,(255, 255, 255),[i*50,j*50,50,50])

            if board[j][i]==1:
                win.blit(queen, (i * 50, j * 50))

            if board[j][i]==2:
                pygame.draw.rect(win, (255, 0, 0), [i * 50, j * 50, 50, 50])

    pygame.display.update()





def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


    for i in range(N):
        for j in range(N):
            if board[i][j]==2:
                board[i][j]=0
    draw(board)


# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens
def isSafe(board, row, col):
    clock = pygame.time.Clock()

    # Check this row on left side
    for i in range(col):
        if board[row][i]==1:
            for j in range(col):
                if board[row][j]==2:
                    board[row][j]=0
            return False
        board[row][i] = 2
        draw(board)
        clock.tick(100)
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            for x, y in zip(range(row, -1, -1),
                            range(col, -1, -1)):
                if board[x][y]==2:
                    board[x][y]=0
            return False

        board[i][j] = 2
        draw(board)
        clock.tick(100)

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            for x, y in zip(range(row, -1, -1),
                            range(col, -1, -1)):
                if board[x][y]==2:
                    board[x][y]=0
            return False
        board[i][j] = 2
        draw(board)
        clock.tick(100)

    return True


def solveNQUtil(board, col):
    # base case: If all queens are placed
    # then return true
    if col >= N:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):

        if isSafe(board, i, col):

            # Place this queen in board[i][col]
            board[i][col] = 1
            draw(board)
            clock = pygame.time.Clock()
            clock.tick(100)

            # recur to place rest of the queens
            if solveNQUtil(board, col + 1) == True:
                return True

            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0
            draw(board)
            clock.tick(100)

    # if the queen can not be placed in any row in
    # this colum col then return false
    return False


# This function solves the N Queen problem using
# Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns false if queens
# cannot be placed, otherwise return true and
# placement of queens in the form of 1s.
# note that there may be more than one
# solutions, this function prints one of the
# feasible solutions.
def solveNQ(board):
    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    # return True


# Driver Code
# solveNQ()

def main():
    run= True
    board = np.zeros((N, N), dtype=int)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solveNQ(board)
        draw(board)
main()
