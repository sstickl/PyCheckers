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

# set_game_board(game_board)
# sets a checkers game board to the size of game_board
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

# game_draw(game_board)
# draws the game board
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

# check_move_valid(int, int, int, int, game_board, int)
# checks if a move is a valid chess move.
# TODO: Add king pieces
def check_move_valid(x_origin, y_origin, x_dest, y_dest, game_board, team):
    #check diagnal
    if team == 1 and (( x_dest == (x_origin + 1) or x_dest == (x_origin-1)) and (y_dest == (y_origin + 1))):
        if game_board[x_dest][y_dest] == 0 or game_board[x_dest][y_dest] == 2:
            return True
    return False
    
def player_move(game_board):
    move_invalid = True

    while move_invalid:
        print("Select a piece to move")
        xo_sel = input("Enter x coordinate: ")
        yo_sel = input("Enter y coordinate: ")
        xo_sel = int(xo_sel) - 1    #humans don't enter block 0
        yo_sel = int(yo_sel) - 1    #humans don't enter block 0
        if game_board[xo_sel][yo_sel] == 1:
            move_invalid = False
        else:
            print("Your piece is not in selected area.  Try again.")

    move_invalid = True
 
    while move_invalid:   
        print("Select an area to move to:")
        xd_sel = input("Enter x coordinate: ")
        yd_sel = input("Enter y coordinate: ")
        xd_sel = int(xd_sel) - 1    #humans don't enter block 0
        yd_sel = int(yd_sel) - 1    #humans don't enter block 0
        if check_move_valid(xo_sel, yo_sel, xd_sel, yd_sel, game_board, 1):
            move_invalid = False
        else:
            print("Invalid destination.  Try again.")

        print("Move: " + str(xo_sel) + "." + str(yo_sel) + " -> " + str(xd_sel) + "." + str(yd_sel))

    game_board[xo_sel][yo_sel] = 0
    game_board[xd_sel][yd_sel] = 1

    return game_board

def cpu_move(game_board):
    return

#main
game_board = gen_blank_matrix(BOARD_WIDTH, BOARD_HEIGHT)
game_board = set_game_board(game_board)
game_draw(game_board)
player_move(game_board)
game_draw(game_board)