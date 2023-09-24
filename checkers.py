# PyCheckers
# See attached GNU LGPLv3 License & Readme file for more details

#===Imports
import os       #OS specific features such as clearing the terminsal
import random   #For functions such as first move/AI

#===Globals
BOARD_WIDTH     = 8
BOARD_HEIGHT    = 8
PLAYER1_ICON    = "o"
PLAYER1_BIGICON = "O"
PLAYER2_ICON    = "x"
PLAYER2_BIGICON = "X"

#===Functions
# gen_blank_matrix
# Generates and returns a blank matrix of [Y][X] size
def gen_blank_matrix(Y, X):
    return [[0] * Y for Z in range(X)]

def isEven(number):
    if number % 2 == 0:
        return True
    return False

#butnotone
def is_within_one(number1, number2):
    match (number1 - number2):
        case 0: return True
        case 1: return True
        case -1: return True
    return False

# set_game_board(game_board)
# sets a checkers game board to the size of game_board
def set_game_board(game_board):
    for y in range (0, int(len(game_board)/2)-1):
        for x in range(0, len(game_board[y])):
            if (x+y) % 2:
                game_board[y][x] = 1
    for y in range (int(len(game_board)/2)+1, len(game_board)):
        for x in range(0, len(game_board[y])):
            if not (x+y) % 2:
                game_board[y][x] = 2

    return game_board

# game_draw(game_board)
# draws the game board
def game_draw(game_board):
    #forward to upgraded draw function with -1 flags
    draw_valid_board(-1, -1, game_board)

# check_move_valid(int, int, int, int, game_board, int)
# checks if a move is a valid chess move.
# TODO: Add king pieces
def check_move_valid(x_origin, y_origin, x_dest, y_dest, game_board, team):
    #Original Pieces Logic
    if not isEven(team) and (((( x_dest == (x_origin + 1)) or x_dest == (x_origin-1))) and (y_dest == (y_origin + 1))):
        if isEven(game_board[y_dest][x_dest]):
            return True
    elif not isEven(team) and ((x_dest == x_origin) and ( y_dest == y_origin+1)) and isEven(game_board[y_dest][x_dest]) and not game_board[y_dest][x_dest] == 0 :#game_board[y_dest][x_dest] == 2:
        return True
    if isEven(team) and ((( x_dest == (x_origin + 1) or x_dest == (x_origin-1))) and (y_dest == (y_origin - 1))):
        if not isEven(game_board[y_dest][x_dest]) or game_board[y_dest][x_dest] == 0:
            return True
    elif isEven(team) and ((x_dest == x_origin) and ( y_dest == y_origin-1)) and not isEven(game_board[y_dest][x_dest]):#(game_board[y_dest][x_dest] == 1):
        return True
    #King Logic
    if ( team == 3 or team == 4 ) and is_within_one(x_origin, x_dest) and is_within_one(y_origin, y_dest) and not ( x_origin == x_dest and y_origin == y_dest ):
        return True

    return False

def draw_valid_board(x_origin, y_origin, game_board):
    team = game_board[y_origin][x_origin]

    #clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    #print the top of the board
    print(" ┏━", end="")
    for c in range(0, BOARD_WIDTH):
        print("━" + str(c+1) + "━", end="")
    print("┓")

    #blank line
    print(" ┃ ", end="")
    for x in range(0, BOARD_WIDTH):
        print("   ", end="")
    print("┃")

    #print the meat and potatoes
    for y in range(0, len(game_board)):
        print(" " + str(y+1), end = " ")
        for x in range(0, len(game_board[y])):
            if ( not x_origin == -1 ) and check_move_valid(x_origin, y_origin, x, y, game_board, team):
                if game_board[y][x] == 0:
                    print(" M ", end = "")
                elif not game_board[y][x] == team:
                    print(" E ", end = "")
            elif game_board[y][x] == 0:
                if (x+y) % 2:
                    print(" ▒ ", end="")
                else:
                    print(" ▓ ", end="")
            elif game_board[y][x] == 1:
                print(" ", end="")
                print(PLAYER1_ICON, end=" ")
            elif game_board[y][x] == 2:
                print(" ", end="")
                print(PLAYER2_ICON, end=" ")
            elif game_board[y][x] == 3:
                print(" ", end="")
                print(PLAYER1_BIGICON, end=" ")
            elif game_board[y][x] == 4:
                print(" ", end="")
                print(PLAYER2_BIGICON, end=" ")
            else:
                print(" E ", end="")
        print("┃")

        #blank line
        print(" ┃ ", end="")
        for x in range(0, len(game_board[y])):
            print("   ", end="")
        print("┃")

    #print the bottom of the board
    print(" ┗━", end="")
    for c in range(0, BOARD_WIDTH):
        print("━━━", end="")
    print("┛")
    
def player_move(game_board, team):
    print("Player " + str(team) + "'s turn!")
    move_invalid = True

    while move_invalid:
        print("Select a piece to move")
        xo_sel = input("Enter x coordinate: ")
        yo_sel = input("Enter y coordinate: ")
        xo_sel = int(xo_sel) - 1    #humans don't enter block 0
        yo_sel = int(yo_sel) - 1    #humans don't enter block 0
        if game_board[yo_sel][xo_sel] == 0:
            pass
        elif isEven(game_board[yo_sel][xo_sel]) == isEven(team):
            move_invalid = False
        else:
            print("Your piece is not in selected area.  Try again.")

    team = game_board[yo_sel][xo_sel]
    draw_valid_board(xo_sel, yo_sel, game_board)

    move_invalid = True
 
    while move_invalid:   
        print("Select an area to move to:")
        xd_sel = input("Enter x coordinate: ")
        yd_sel = input("Enter y coordinate: ")
        xd_sel = int(xd_sel) - 1    #humans don't enter block 0
        yd_sel = int(yd_sel) - 1    #humans don't enter block 0
        print("Move: " + str(xo_sel) + "." + str(yo_sel) + " -> " + str(xd_sel) + "." + str(yd_sel))
        if check_move_valid(xo_sel, yo_sel, xd_sel, yd_sel, game_board, team):
            move_invalid = False
        else:
            print("Invalid destination.  Try again.")

    game_board[yo_sel][xo_sel] = 0

    if team == 1 and yd_sel == (BOARD_HEIGHT-1):
        team = 3
    elif team == 2 and yd_sel == 0:
        team = 4

    game_board[yd_sel][xd_sel] = team

    return game_board

def cpu_move(game_board):
    return

def check_winner(game_board):
    count_player1 = 0
    count_player2 = 0

    for y in range (0, len(game_board)):
        for x in range(0, len(game_board[y])):
            if game_board[y][x] == 0:
                pass    #don't count 0
            elif not isEven(game_board[y][x]):
                count_player1 = count_player1 + 1
            elif isEven(game_board[y][x]):
                count_player2 = count_player2 + 1

    if count_player1 == 0:
        return 2
    elif count_player2 == 0:
        return 1
    return 0

#main
game_board = gen_blank_matrix(BOARD_WIDTH, BOARD_HEIGHT)
game_board = set_game_board(game_board)

while check_winner(game_board) == 0:
    game_draw(game_board)
    player_move(game_board, 1)
    game_draw(game_board)
    player_move(game_board, 2)

game_draw(game_board)
print("The winner is player: " + str(check_winner(game_board)))