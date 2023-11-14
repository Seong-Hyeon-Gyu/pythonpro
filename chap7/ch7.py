import random
display_instruct()
turn = X
board = new_board()
display_board(board)
while not winner(board):
    if turn == human:
        move = human_move(board, human)
        board[move] = human
    else:
        move = cmptr_mv(board,hmn,cmptr)
        board[move] = computer
    display_board(board)
    turn = next_turn(turn)
winner = winner(board)
congrat_winner(winner,human,computer)
def display_instruct():
    print("\tWelcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.\n\tThis will be a showdown between your human brain and my silicon procesor.\n\n\n\tYou will make our move known by entering a number, 0 - 8. The number willcorrespond to the board position as ilustrated:")
    print("\n\t\t\t\t0 | 1 | 2\n\t\t\t\t---------\n\t\t\t\t3 | 4 | 5\n\t\t\t\t---------\n\t\t\t6 | 7 | 8\n")
    print("\nPrepare your self, human. The ultimate batter is about to begin.\n\n\n")
    ask_yes_no()
def new_board():
    grid = [" " for x in range(9)]
def display_board(board):
    for r in range(3):
        if (r==0):
            rownum = r
        elif (r==1):
            rownum = r+2
        else:
            rownum = r+4
        print("\t\t", grid[rownum], "| ", grid[rownum+1], "| ", grid[rownum+2])
        if (r!=2):
            print("\t\t---|---|---")
def winner(board):
    human = X
    computer = O
    if grid[0] == grid[1] == grid[2] or \
       grid[3] == grid[4] == grid[5] or \
       grid[6] == grid[7] == grid[8] or \
       grid[0] == grid[3] == grid[6] or \
       gird[1] == grid[4] == grid[7] or \
       gird[2] == grid[5] == grid[8] or \
       gird[0] == grid[4] == gird[8] or \
       gird[2] == gird[4] == gird[6]:
        return True
    else:
        return False
def human_move(board, human):
    num = int(input("Where will you move? <0 - 8>:"))
    legal_move()

def computer_move(board, human, computer):
    randnum = random.random(0, 9)
    if grid[randnum]!=" " and grid[randnum]==X:
        computer_move()
    else:
        grid[randnum]=computer
def next_turn(turn):
    if (turn == X):
        turn = O
    return turn
def congrat_winner(winner, human, computer):
    if count == 10:
        print("draw")
    else:
        if turn == X:
            print("No, no! It cannot be! Somehow you tricked me, human.\nBut never again! I, the computer, so swear it!")
        else:
            print("As I predicted, human, I am triumphant once more.\nProof that computers are superior to humans in all regards.")
def ask_yes_no(question):
    global turn
    while true:
        question = input("Do you require the first move? <y/n>:")
        if (question == 'y'):
            turn = X
            break
        elif (quesion == 'x'):
            trun = O
            break
def ask_number(question, low, high):
    question = int(input("Where will you move? <0 - 8>:"))
    print("Fine..")
def legal_move(board):
    if grid[num]!=" ":
        print("Try input again.")
        if turn == X:
            human_move()
        else:
            computer_move()
