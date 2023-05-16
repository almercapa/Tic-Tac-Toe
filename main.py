import random

#Global Variables
board = [["-","-","-"],["-","-","-"],["-","-","-"]]
player = "X"

def print_board():
    print("\n\t0\t1\t2")
    print("\n0\t" + board[0][0] + "\t" + board[0][1] + "\t" + board[0][2])
    print("\n1\t" + board[1][0] + "\t" + board[1][1] + "\t" + board[1][2])
    print("\n2\t" + board[2][0] + "\t" + board[2][1] + "\t" + board[2][2] + "\n")


#returns true if a row,col on the board is open
def is_valid_move(row, col):
    if board[row][col] == "-":
        return True
    return False

#places player on row,col on the board
def place_player(player, row, col):
    board[row][col] = player;


# returns true if player has won in any of the three columns. A player wins if they
# have three consecutive X's or O's in a column.
def check_col_win(player):
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    return False

# returns true if player has won in any of the three rows. A player wins if they
# have three consecutive X's or O's in a row.
def check_row_win(player):
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    return False

# returns true if player has won in either diagonal directions. A player wins if they
# have three consecutive X's or O's in a diagonal.
def check_diag_win(player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# returns true if player has won the game
def check_win(player):
    if check_col_win(player) == True or check_row_win(player) == True or check_diag_win(player) == True:
        return True
    return False

# returns true if all spots on the board is filled
def check_tie():
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O" or board[i][j] == "X":
                count = count + 1
    if count >= 9:
        return True
    return False
    
def minimax(player):
    optimalRow = -1
    optimalCol = -1
    #copy your basecase here:
    if check_win("O"):
        return (10, None, None)
    elif check_win("X"):
        return (-10, None, None)
    elif check_tie():
        return (0, None, None)

    #implement recursive case
    if player == "O":
        best = -1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    place_player("O", row, col)
                    moveVal = (minimax("X")[0])
                    if (moveVal > best):
                        best = moveVal
                        optimalRow = row
                        optimalCol = col
                    place_player("-", row, col)
        return (best, optimalRow, optimalCol)
    if player == "X":
        worst = 1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-":
                    place_player("X", row, col)
                    moveVal = (minimax("O")[0])
                    if (moveVal < worst):
                        worst = moveVal
                        optimalRow = row
                        optimalCol = col
                    place_player("-", row, col)
        return (worst, optimalRow, optimalCol)

#Asks the user to enter a row and col until the user enters a valid location
#Adds user location to the board, and prints the board
def take_turn(player):
    row = 4
    col = 4
    print(player + "'s Turn")
    if player == "X":
        while row >= 3 or row < 0 or col >= 3 or col < 0:
            row = int(input("Enter a row "))
            col = int(input("Enter a col "))
            if row >= 3 or row < 0 or col >= 3 or col < 0:
                print("Please enter a valid move")
            else:
                if is_valid_move(row, col) == True:
                    place_player(player, row, col)
                    print_board()
                else:
                    print("Please enter a valid move")
                    row = 4
                    col = 4
    else:
        score, row, col = minimax("O")
        if is_valid_move(row, col) == True:
            place_player(player, row, col)
            print_board()
        else:
            while is_valid_move(row, col) == False:
                row = random.randint(0,2)
                col = random.randint(0,2)
                if is_valid_move(row, col) == True:
                    place_player(player, row, col)
                    print_board()
                    break

#Start of program
print("\t\tWelcome to Tic Tac Toe!")
print_board()

while check_tie() == False:
    take_turn(player)
    # breaks loop and announces winner if the check_win method returns true
    if check_win(player) == True:
        break
    else:
        # changes player variable
        if player == "X":
            player = "O"
        else:
            player = "X"

# prints winner
if check_win(player) == True:
    print(player + " Wins!")
else:
    print("It's a tie!")
