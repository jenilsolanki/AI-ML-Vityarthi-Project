import math

board = []
for _ in range(9):
    board.append(" ")
print(board)

# Guide board to show positions
def position_guide():
    print("\nPosition Guide : ")
    print(" 0 | 1 | 2 ")
    print("-----------")
    print(" 3 | 4 | 5 ")
    print("-----------")
    print(" 6 | 7 | 8 \n")

def print_board():
    print("\nCurrent Board : ")
    for i in range(3):
        print(board[3*i], "|", board[3*i+1], "|", board[3*i+2])
        if i<2 :
            print("-----------")
    print()

def available_moves_alternative(b):
    moves = []
    for i, position in enumerate(b):
        if position == " ":
            moves.append(i)
    return moves

def winner(b1):
    win_condition = [[0,1,2],[3,4,5],[6,7,8],
                     [0,3,6],[1,4,7],[2,5,8],
                     [0,4,8],[2,4,6]]
    for a,b,c in win_condition :
        if board[a] == board[b] == board[c] and board[a] != " " :
            return board[a]
    return None

def is_full(b1) :
    return " " not in b1

def minimax(b1, is_maximizing):
    win = winner(b1)
    if win == "0" : 
        return 1
    if win == "X" : 
        return -1 
    if is_full(b1):
        return 0
    if is_maximizing :
        best = -math.inf
        for move in available_moves_alternative(b1):
            b1[move] = "0"
            score = minimax(b1,False)
            b1[move] = " "
            best = max(best,score)
        return best
    else : 
        best = -math.inf
        for move in available_moves_alternative(b1):
            b1[move] = "X"
            score = minimax(b1,True)
            b1[move] = " "
            best = max(best,score)
        return best
    
def best_move():
    best_score = -math.inf
    move = None
    for m in available_moves_alternative(board):
        board[m] = "0"
        score = minimax(board, False)
        board[m] = " "
        if score > best_score :
            best_score = score
            move = m
    return move

print("Tic Tac Toe - You are X, AI is 0")
position_guide()

# Ask user who wants to play first

choice = input("Do you want to play first?\n 1 = Yes \n 2 = No \n Enter : ")
if choice == "2":
    ai = best_move()
    board[ai] = "0"
    print(f"\nAI palyed first at position {ai}")

# Main Game Loop
while True :
    print_board()

    # User Move
    user = int(input("Enter your move (0-8) : "))
    if user not in range(9) or board[user] != " " :
        print("Invalid move. Try again.")
        continue

    board[user] = "X"

    if winner(board) == "X":
        print_board()
        print("🎊 You win!")
        break

    if is_full(board):
        print_board()
        print("It's a tie!")
        break

    # AI MOVE
    ai = best_move()
    board[ai] = "0"
    print(f"\nAI played at position {ai}")

    if winner(board) == "0":
        print_board()
        print("🎰 AI wins!")
        break

    if is_full(board) :
        print_board()
        print("It's a tie!")
        break
