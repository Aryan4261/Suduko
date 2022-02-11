# Game Board
board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]
player_symbol = ["X", "O"]


def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--|---|---")
    print(board[3], "|", board[4], "|", board[5])
    print("--|---|---")
    print(board[6], "|", board[7], "|", board[8])


def player_input(player):
    correct_input = True
    org_position = input \
        ("Player {player_number}'s chance! Choose position to fill {symbol} [1-9] : ".format(player_number=player + 1,
                                                                                       symbol=player_symbol[player]))
    if org_position == "":
        print("Enter a valid input")
        player_input(player)
    else:
        op = int(org_position)
        position = op - 1
        if board[position] == "X" or board[position] == "O":
            correct_input = False
        if not correct_input:
            print("Position occupied")
            player_input(player)
        else:
            board[position] = player_symbol[player]


def check_win():
    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for check in winning_positions:
        win_symbol = board[check[0]]
        if win_symbol != " ":
            won = True
            for point in check:
                if board[point] != win_symbol:
                    won = False
                    break

            if won:
                if win_symbol == player_symbol[0]:
                    print("Player 1 Won!!!")
                else:
                    print("Player 2 Won!!!")
                break

        else:
            won = False
    return won


def space():
    if board.count("X") + board.count("O") != 9:
        return True
    else:
        return False


player = 0
while space() and not (check_win()):
    print_board()
    player_input(player)
    check_win()
    space()
    player = int(not player)

if check_win() is False:
    print("It's a Tie!!")# Game Board
board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]
player_symbol = ["X", "O"]


def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--|---|---")
    print(board[3], "|", board[4], "|", board[5])
    print("--|---|---")
    print(board[6], "|", board[7], "|", board[8])


def player_input(player):
    correct_input = True
    org_position = input \
        ("Player {player_number}'s chance! Choose position to fill {symbol} [1-9] : ".format(player_number=player + 1,
                                                                                       symbol=player_symbol[player]))
    if org_position == "":
        print("Enter a valid input")
        player_input(player)
    else:
        op = int(org_position)
        position = op - 1
        if board[position] == "X" or board[position] == "O":
            correct_input = False
        if not correct_input:
            print("Position occupied")
            player_input(player)
        else:
            board[position] = player_symbol[player]


def check_win():
    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for check in winning_positions:
        win_symbol = board[check[0]]
        if win_symbol != " ":
            won = True
            for point in check:
                if board[point] != win_symbol:
                    won = False
                    break

            if won:
                if win_symbol == player_symbol[0]:
                    print("Player 1 Won!!!")
                else:
                    print("Player 2 Won!!!")
                break

        else:
            won = False
    return won


def space():
    if board.count("X") + board.count("O") != 9:
        return True
    else:
        return False


player = 0
while space() and not (check_win()):
    print_board()
    player_input(player)
    check_win()
    space()
    player = int(not player)

if check_win() is False:
    print("It's a Tie!!")