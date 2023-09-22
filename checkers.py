# PyCheckers
# See attached GNU LGPLv3 License & Readme file for more details

#===Imports
import os       #OS specific features such as clearing the terminsal
import random   #For functions such as first move/AI

#===Globals
BOARD_WIDTH  = 8
BOARD_HEIGHT = 8
PLAYER1_ICON = "O"
PLAYER2_ICON = "X"

#===Functions
# gen_blank_matrix
# Generates and returns a blank matrix of X, Y size
def gen_blank_matrix(X, Y):
    return [[0] * X for Z in range(Y)]

# set_game_board
# sets a checkers game board
def set_game_board(game_board):
    for x in range (0, int(len(game_board)/2)-1):
        for y in range(0, len(game_board[x])):
            if (x+y) % 2:
                game_board[x][y] = 1
    for x in range (int(len(game_board)/2)+1, len(game_board)):
        for y in range(0, len(game_board[x])):
            if not (x+y) % 2:
                game_board[x][y] = 2

    return game_board

def game_draw(game_board):
    #clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    #print the top of the board
    print("┏━", end="")
    for c in range(0, BOARD_WIDTH):
        print("━━━", end="")
    print("┓")

    #print the meat and potatoes
    for x in range(0, len(game_board)):
        print("┃", end=" ")
        for y in range(0, len(game_board[x])):
            if game_board[x][y] == 0:
                if (x+y) % 2:
                    print(" ▒ ", end="")
                else:
                    print(" ▓ ", end="")
            elif game_board[x][y] == 1:
                print(" ", end="")
                print(PLAYER1_ICON, end=" ")
            elif game_board[x][y] == 2:
                print(" ", end="")
                print(PLAYER2_ICON, end=" ")
            else:
                print(" E ", end="")
        print("┃")

        #blank line
        print("┃ ", end="")
        for y in range(0, len(game_board[x])):
            print("   ", end="")
        print("┃")

    #print the bottom of the board
    print("┗━", end="")
    for c in range(0, BOARD_WIDTH):
        print("━━━", end="")
    print("┛")

    
def player_move(game_board):
    x_sel = input("Enter x coordinate of the player's move: ")
    y_sel = input("Enter y coordinate of the player's move: ")
    x_sel = int(x_sel)
    y_sel = int(y_sel)

    game_board[x_sel][y_sel] = 1
    return game_board

def cpu_move(game_board):
    return

#main
game_board = gen_blank_matrix(BOARD_WIDTH, BOARD_HEIGHT)
game_board = set_game_board(game_board)
game_draw(game_board)
#player_move(game_board)
#game_draw(game_board)