#!/usr/local/bin/python3

#
#
# Deshawn Dana
# Tic Tac Toe using Pygame
#
#

import pygame
from random import randint
from pygame.locals import *


Table = [ [None,None,None] , [None,None,None] , [None,None,None]]
turns = 1
winner = None
gameExit = False


#################################### logic for drawing item on screen) ######################################
## this function determines the position of which square was clicked in order to draw corresponding item ##
############################################################################################################
def drawItem(clickedPosition, xo):

    x,y = clickedPosition
    
    font = pygame.font.Font(None, 100)
    text = font.render(xo, True, (white))
    
    if x < 100 and y < 100:
        print("you have clicked the square 1")
        
        textpos = text.get_rect()
        screen.blit(text, (25,25))
        Table[0][0] = xo
    elif x > 100 and x < 200 and y < 100:
        print("you have clicked the square 2")
        
        textpos = text.get_rect()
        screen.blit(text, (125,25))
        Table[0][1] = xo
    elif x > 200 and y < 100:
        print("you have clicked the square 3")
        
        textpos = text.get_rect()
        screen.blit(text, (225,25))
        Table[0][2] = xo

    elif x < 100 and y > 100 and y < 200:
        print("you have clicked the square 4")

        textpos = text.get_rect()
        screen.blit(text, (25,125))
        Table[1][0] = xo
    
    elif x > 100 and x < 200 and y > 100 and y < 200:
        print("you have clicked the square 5")
        
        textpos = text.get_rect()
        screen.blit(text, (125,125))
        Table[1][1] = xo
    elif x > 200 and y > 100 and y < 200:
        print("you have clicked the square 6")
        
        textpos = text.get_rect()
        screen.blit(text, (225,125))
        Table[1][2] = xo

    elif x < 100 and y > 200:
        print("you have clicked the square 7")
        
        textpos = text.get_rect()
        screen.blit(text, (25,225))
        Table[2][0] = xo
    elif x > 100 and x < 200 and y > 200:
        print("you have clicked the square 8")
        
        textpos = text.get_rect()
        screen.blit(text, (125,225))
        Table[2][1] = xo
    elif x > 200 and y > 200:
        print("you have clicked the square 9")
        
        textpos = text.get_rect()
        screen.blit(text, (225,225))
        Table[2][2] = xo

    pygame.display.flip()

############################################################################################################
## Checks for winner, if winner is found, display winner message on screen #################################
############################################################################################################
def CheckWin(xo):
    winner = False
    
    ##horizontal logic
    if Table[0][0] == "X" and Table[0][1] == "X" and Table[0][2] == "X":
        print("PLAYER 1 WINS")
        displayWinner(xo,winner)
        winner = True
    elif Table[0][0] == "O" and Table[0][1] == "O" and Table[0][2] == "O":
        print("CPU WINS")
        displayWinner(xo,winner)
        winner = True
    elif Table[1][0] == "X" and Table[1][1] == "X" and Table[1][2] == "X":
        print("PLAYER 1 WINS")
        displayWinner(xo,winner)
        winner = True
    elif Table[1][0] == "O" and Table[1][1] == "O" and Table[1][2] == "O":
        print("CPU WINS")
        displayWinner(xo,winner)
        winner = True
    elif Table[2][0] == "X" and Table[2][1] == "X" and Table[2][2] == "X":
        print("PLAYER 1 WINS")
        displayWinner(xo,winner)
        winner = True
    elif Table[2][0] == "O" and Table[2][1] == "O" and Table[2][2] == "O":
        print("CPU WINS")
        displayWinner(xo,winner)
        winner = True

    ## Vertical Logic
    if Table[0][0] == "X" and Table[1][0] == "X" and Table[2][0] == "X":
        print("PLAYER 1 WINS")
        displayWinner(xo,winner)
        winner = True
    elif Table[0][0] == "O" and Table[1][0] == "O" and Table[2][0] == "O":
        print("CPU WINS")
        displayWinner(xo,winner)
        winner = True
    elif Table[0][1] == "X" and Table[1][1] == "X" and Table[2][1] == "X":
        print("PLAYER 1 WINS")
        displayWinner(xo,winner)
        winner = True
    elif Table[0][1] == "O" and Table[1][1] == "O" and Table[2][1] == "O":
        print("CPU WINS")
        displayWinner(xo,winner)
        winner = True
    elif Table[0][2] == "X" and Table[1][2] == "X" and Table[2][2] == "X":
        print("PLAYER 1 WINS")
        displayWinner(xo,winner)
        winner = True
    elif Table[0][2] == "O" and Table[1][2] == "O" and Table[2][2] == "O":
        print("CPU WINS")
        displayWinner(xo,winner)
        winner = True

    ## Diagonal Logic
    if Table[0][0] == "X" and Table[1][1] == "X" and Table[2][2] == "X":
        print("PLAYER 1 WINS")
        displayWinner(xo,winner)
        winner = True
    elif Table[0][0] == "O" and Table[1][1] == "O" and Table[2][2] == "O":
        print("CPU WINS")
        displayWinner(xo,winner)
        winner = True
    elif Table[0][2] == "X" and Table[1][1] == "X" and Table[2][0] == "X":
        print("PLAYER 1 WINS")
        displayWinner(xo,winner)
        winner = True
    elif Table[0][2] == "O" and Table[1][1] == "O" and Table[2][0] == "O":
        print("CPU WINS")
        displayWinner(xo,winner)
        winner = True

    # if there is no winner, display stale mate message
    if turns > 9:
        displayWinner(xo, winner)




def displayWinner(xo, winner):

    screen2 = pygame.display.set_mode((300,300))
    screen2.fill([0,0,0])
    
    if xo == "X" and turns < 10 or winner == True:
        font = pygame.font.Font(None, 50)
        text = font.render("Player 1 Wins", 1, (255,255,255))
        # copy the rendered message onto the board
        screen2.fill ((255, 255, 255), (0, 300, 300, 25))
        screen2.blit (text, (10, 150))
        pygame.display.flip()
    elif xo =="O" and turns < 10 or winner == True:
        font = pygame.font.Font(None, 50)
        text = font.render("Player 2 Wins", 1, (255,255,255))
        # copy the rendered message onto the board
        screen2.fill ((255, 255, 255), (0, 300, 300, 25))
        screen2.blit (text, (10, 150))
        pygame.display.flip()
    elif turns > 9 and winner == False :
        font = pygame.font.Font(None, 50)
        text = font.render("STALE MATE", 1, (255,255,255))
        # copy the rendered message onto the board
        screen2.fill ((255, 255, 255), (0, 300, 300, 25))
        screen2.blit (text, (10, 150))
        pygame.display.flip()


#################################################################################################
############################### initializes the board ############################################

pygame.init()
black = (0,0,0)
white = (255,255,255)

screen = pygame.display.set_mode((300,300))
pygame.display.set_caption("TicTacToe")
screen.fill([0,0,0])

#construct lines for tic tac toe board
pygame.draw.line(screen,white,(100,300),(100,0),4)
pygame.draw.line(screen,white,(200,300),(200,0),4)
pygame.draw.line(screen,white,(300,100),(0,100),4)
pygame.draw.line(screen,white,(300,200),(0,200),4)

pygame.display.flip()

##################################################################################################

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.MOUSEBUTTONDOWN: #if the user clicks, its going to detect it
            clickedPosition = pygame.mouse.get_pos()
            turns = turns+1
            if turns % 2 == 0:
                #player 1
                xo = "X"
            else:
                #player 2
                xo = "O"
            drawItem(clickedPosition, xo)
            CheckWin(xo)
            print(turns, " this is turns")
            print(clickedPosition, "Current Position")
            print(Table)


pygame.quit()
quit()








