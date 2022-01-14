# CSE 210 - W02 Prove: Developer - Solo Code Submission
# Tic Tac Toe

CRED = '\033[91m'
CGRN = '\033[92m'
CYEL = '\033[93m'
CBLU = '\033[94m'
CEND = '\033[0m'

def create_board(length, auto = False):
    board = []
    num = 1
    for _ in range(length):
        row = []
        for _ in range(length):
            x = "-"
            if auto:
                x = num
                num+=1
            row.append(x)

        board.append(row)
    return board

def print_board(board):
    print()
    for i in range(len(board)):
        row = board[i]
        for j in range(len(board)):
            print(" ", end = "")
            print(row[j], end = "")
            if j < len(board) - 1:
                print(" |", end = "")
        if i < (len(board)-1):
            print("\n---+---+---")

def update_board(board, reference, number, symbol):
    for i in range(len(reference)):
        row = reference[i]
        for j in range(len(reference)):
            if row[j] == number:
                myRow = board[i]
                myRow[j] = symbol

def check_win(available):
    # Horizontal Win 1
    if available[0] == available [1] == available [2]:
        print(f"\n\n{CGRN}Congratulations. Player {available[0]} wins!{CEND} Thanks for playing")
        return True

    # Horizontal Win 2
    if available[3] == available [4] == available [5]:
        print(f"\n\n{CGRN}Congratulations. Player {available[3]} wins!{CEND} Thanks for playing")
        return True
    
    # Horizontal Win 3
    if available[6] == available [7] == available [8]:
        print(f"\n\n{CGRN}Congratulations. Player {available[6]} wins!{CEND} Thanks for playing")
        return True

    # Vertical Win 1
    if available[0] == available [3] == available [6]:
        print(f"\n\n{CGRN}Congratulations. Player {available[0]} wins!{CEND} Thanks for playing")
        return True

    # Vertical Win 2
    if available[1] == available [4] == available [7]:
        print(f"\n\n{CGRN}Congratulations. Player {available[1]} wins!{CEND} Thanks for playing")
        return True

    # Vertical Win 3
    if available[2] == available [5] == available [8]:
        print(f"\n\n{CGRN}Congratulations. Player {available[2]} wins!{CEND} Thanks for playing")
        return True

    # Diagonal Win 1
    if available[0] == available [4] == available [8]:
        print(f"\n\n{CGRN}Congratulations. Player {available[0]} wins!{CEND} Thanks for playing")
        return True

    # Diagonal Win 2
    if available[2] == available [4] == available [6]:
        print(f"\n\n{CGRN}Congratulations. Player {available[2]} wins!{CEND} Thanks for playing")
        return True


def main():
    print("\n\n > > > Welcome to Tic Tac Toe Game < < <")

    # Explain Reference
    print("\nFor this game, you should choose one of these slots:")

    example_board = create_board(3,True)
    print_board(example_board)

    # Set the game board
    board = create_board(3)

    # Start game
    win = False
    available = ['1','2','3','4','5','6','7','8','9']
    nturns = 0
    while win == False:
        # Player X choose a slot
        choice = int(input(f"\n\n{CBLU}Player X{CEND} Please choose one slot: "))
        while str(choice) not in available:
            choice = int(input(f"\n{CRED}Unavailable Spot{CEND}\n{CBLU}Player X{CEND} Please choose an available slot: "))

        update_board(board, example_board, choice, "X")
        available.insert(choice, "X")
        available.pop(choice - 1)
        nturns+=1

        # Print Updated Board
        print_board(board)

        if check_win(available):
            break

        if nturns > 8:
            print(f"\n\n{CGRN}It's a tie!{CEND} Thanks for playing.")
            break

        # Player O choose a slot
        choice = int(input(f"\n\n{CYEL}Player O{CEND} Please choose one slot: "))
        while str(choice) not in available:
            choice = int(input(f"\n{CRED}Unavailable Spot{CEND}\n{CYEL}Player O{CEND} Please choose an available slot: "))

        update_board(board, example_board, choice, "O")
        available.insert(choice, "O")
        available.pop(choice - 1)   
        nturns+=1         

        # Print Updated Board
        print_board(board)

        if check_win(available):
            break

    print("\n")

if __name__ == "__main__":
    main()