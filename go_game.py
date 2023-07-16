# -*- coding: utf-8 -*-
import os
import sys
import settings_form
from settings_form import board_size, handicap, komi, board_style


board_9x9 = [
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
]


board_13x13 = [
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
]


board_19x19 = [
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
]

# boards lookup
BOARDS = {
     '9': board_9x9,
    '13': board_13x13,
    '19': board_19x19
}

TRANSLATE = { 
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g":  6,
    "h":  7,
    "j":  8,
    "k":  9,
    "l":  10,
    "m":  11,
    "n":  12,
    "o":  13,
    "p":  14,
    "q":  15,
    "r":  16,
    "s":  17,
    "t":  18

}

# stuff
liberties = []
group = []
groups = []
black_turn = True
black_points = 0
white_points = 0

#properties from settings_form
_handicap = int(handicap)
_komi = float(komi)
_board_size = int(board_size)
_board_style = board_style

#spaces
SPACES9  = "            "
SPACES13 = "                    "
SPACES19 = "                                "           


# stones
EMPTY = 0
BLACK = 1
WHITE = 2

MARKER = 4
OFFBOARD = 7
LIBERTY = 8

BLACK_MARKED = 5
WHITE_MARKED = 6

# current board used
board = None


HANDICAP = [[4, 4] , [_board_size - 3, _board_size - 3], [_board_size - 3, 4] , [4, _board_size - 3], [int(_board_size  / 2 ) + 1, int(_board_size /2) + 1]]
# GO ban size
BOARD_WIDTH = 0
BOARD_RANGE = 0
MARGIN = 2

# notation
notation = '     a b c d e f g h j k l m n o p q r s t'

# representation of stones
if _board_style == '*': pieces = '*\u2B24\u25EF  bw +'
else: pieces = '·\u2B24\u25EF  bw +'

# ●○ ⚪⚫ ⚪🟩  🔵〇⬤○◯


def print_board():
    
    for row in range(BOARD_RANGE):
        for col in range(BOARD_RANGE):
            
            
         
            stone = board[row][col]
            
            # print rank
            if col == 0 and row > 0 and row < BOARD_RANGE - 1:
                rank = BOARD_RANGE - 1 - row
                print(('  ' if rank < 10 else ' ') + str(rank), end='')
        
            print(pieces[stone] + ' ', end='')

        print()
    
    # print notation
    print(notation[0:BOARD_RANGE*2] + '\n')



# setting all spaces to empty
def clear_board():

    for row in range(BOARD_RANGE):
        for col in range(BOARD_RANGE):
            stone = board[row][col]
            if stone == BLACK:
                board[row][col] = EMPTY

            if stone == WHITE:
                board[row][col] = EMPTY
    



# set Go ban size
def set_board_size(size):
    global BOARD_WIDTH, BOARD_RANGE, board
    BOARD_WIDTH = size
    BOARD_RANGE = BOARD_WIDTH + MARGIN
    board = BOARDS[str(size)]

# recursively counting liberties
def count_liberties(x,y, color):

    curr_stone = board[x][y]

    if curr_stone == OFFBOARD:
        return
    if curr_stone != BLACK_MARKED and curr_stone != WHITE_MARKED and curr_stone != LIBERTY and color == curr_stone:
        board[x][y] += MARKER
        
        group.append([x , y])
        
        count_liberties(x , y + 1, color)
        count_liberties(x , y - 1, color)
        count_liberties(x + 1 , y, color)
        count_liberties(x - 1, y, color)
    elif curr_stone == EMPTY:
        liberties.append([x, y])
        board[x][y] = LIBERTY
    else: return
    


def set_stone(row, col, color):
    global black_turn
    if board[row][col] != EMPTY:
        print("  There is already a stone!")
        black_turn = not black_turn
    else:
        if color == BLACK:
            board[row][col] = BLACK
        else:
            board[row][col] = WHITE


def demarked_board ():
    for row in range(BOARD_RANGE):
        for col in range(BOARD_RANGE):
            stone = board[row][col]

            if stone == BLACK_MARKED:
                board[row][col] = BLACK

            if stone == WHITE_MARKED:
                board[row][col] = WHITE

            if stone == LIBERTY:
                board[row][col] = EMPTY

def set_handicap():
    for i in range(_handicap):
        board[HANDICAP[i][0]][HANDICAP[i][1]] = BLACK





def check_board(x_cerrent, y_cerrent):
    global black_turn
    global white_points
    global black_points
    
    # checking if all groups have liberties
    for row in range(BOARD_RANGE):
        for col in range(BOARD_RANGE):
            color = board[row][col]
            if color == BLACK or color == WHITE:

                liberties.clear()
                group.clear()
                
                if [row, col] in groups:
                    continue
                else:
                    count_liberties(row, col, color)
                    for i in group:
                        groups.append(i)
                
                
                # delete all marked stones

                demarked_board()

            # to see all current groups separately on the different Gobans 

            #      print(x_cerrent,y_cerrent)
            #      for i in range(9):
            #          for j in range(9):
            #              if [i + 1, j + 1] in group:
            #                  print(pieces[color], end = " ")
            #              else:
            #                  print(pieces[EMPTY], end = " ")
            #          print()
            #  
            #      print(group)
                
                
                if len(liberties) == 0:
                    if [x_cerrent, y_cerrent] in group:
                        print(f"  Suicide move for {'BLACK' if  color == BLACK else 'WHITE'}!")
                        if color == 1:
                            black_turn = True
                        else:
                            black_turn = False
                        
                        board[x_cerrent][y_cerrent] = EMPTY
                        
                    else:
                        for i in group:
                            board[i[0]][i[1]] = EMPTY
                            if  color == BLACK:
                                white_points+=1
                            else:
                                black_points+=1
    groups.clear()           
                
    
    
                
        
        


# main function
def main():
    
    global black_turn
    global white_points
    global black_points

    # if handicap is bigger than 2 white should go first (official rules)
    if _handicap >= 2:
        black_turn = False
    else: 
        black_turn = True

    
    board_size = _board_size
    white_points = 0
    black_points = 0
   
   
    set_board_size(board_size)
    set_handicap()
    

    # spaces for score
    if board_size == 9: score_space = SPACES9
    elif board_size == 13: score_space = SPACES13
    else: score_space = SPACES19
    
    os.system('cls')
    
    print("Welcome to my version 1.0 of my Game of Go!")
    print("Now it is at most part console-based but i will add some GUI with matplotlib in the next version.")
    print("User commands:")
    print("  stop - to stop the app")
  # print("  count - to count the points on the board")
    print()
    print(f"  ⬤ - BLACK{score_space[0:len(score_space)-10]}◯ - WHITE")
    print("\n     Make your first move!")
    
    # subloop
    while True:
        print_board()
        
        try:
            turn = input(f"  {'BLACK' if  black_turn else 'WHITE'} MOVE: ")
            os.system('cls')

            # stop the program
            if turn == "stop":
                os.system('cls')
                sys.exit()

            # restart the current game
            if turn == "restart":
                os.system('cls')
                clear_board()
                white_points = 0
                black_points = 0
                break
                
           # in thi version count() is in development)
           # if turn == "count":
           #    pass

            # exception handling
            if (len(turn) != 2 and board_size == 9) or (len(turn) not in (2,3) and (board_size == 13 or  board_size == 19)) and turn != "stop":
                print("  Wrong string size! Example: 'f3'")
                continue

            elif (turn[0] not in TRANSLATE.keys() or (int( turn[1]) not in range(1,10) and board_size == 9) or ( int(turn[1:3]) not in range(1,14) and board_size == 13) or (int(turn[1:3]) not in range(1,20)  and board_size == 19)) and turn != "stop" : 
                print("  Wrong format or out of the boundaries of this board size! Example: 'a13'")
                continue
            
            elif turn != "stop":

                # making moves on different board sizes

                if board_size == 9 or len(turn) == 2:

                    move_col = TRANSLATE[turn[0]] + 1
                    move_row =  board_size - int(turn[1]) + 1
                
                else:
                    move_col = TRANSLATE[turn[0]] + 1
                    move_row =  board_size - int(turn[1:3]) + 1
               
                if black_turn: 
                    black_turn = False 
                    set_stone(move_row , move_col , BLACK)
                    
                    

                else: 
                    black_turn = True
                    set_stone(move_row , move_col , WHITE)
                    
                    
        except SystemExit:
            sys.exit()
                
        except:
            os.system('cls')
            print("  Invalid input!")
            continue
            

        
        

        
        
        # checking for "dead" groups of stones and deleting them
        check_board(move_row, move_col)
        # score
        print(f"  B: {black_points}{score_space}W: {white_points} + {_komi}")
        
        print(f"  Last move: {turn[0].upper()}{turn[1:3]}")
        
        
        
    
# main loop
while True:    
    main()
    
