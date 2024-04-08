import random
height = 6
length = 7
minus = '-'
PLAYER_TOKEN = 'X'
AI_TOKEN = 'O'

def create_board():
    return [[minus for _ in range(length)] for _ in range(height)]

def print_board(board):
    for row in board:
        print(' '.join(row))
    print('1 2 3 4 5 6 7')

def is_valid_move(board, column):
    return board[0][column] == minus

def drop_piece(board, column, token):
    for row in range(height-1, -1, -1):
        if board[row][column] == minus:
            board[row][column] = token
            break

def check_win(board, token):
    for row in range(height):
        for col in range(length):
            if col + 3 < length and all(board[row][col + i] == token for i in range(4)):
                return True
            if row + 3 < height and all(board[row + i][col] == token for i in range(4)):
                return True
            if col + 3 < length and row + 3 < height and all(board[row + i][col + i] == token for i in range(4)):
                return True
            if col + 3 < length and row - 3 >= 0 and all(board[row - i][col + i] == token for i in range(4)):
                return True
    return False

def player_move(board):
    while True:
        try:
            column = int(input("Ваш ход (введите номер столбца от 1 до 7): ")) - 1
            if 0 <= column < length and is_valid_move(board, column):
                return column
            else:
                print("Некорректный ход. Попробуйте еще раз.")
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")

def computer_move(board):
    available_length = [col for col in range(length) if is_valid_move(board, col)]
    return random.choice(available_length)

board = create_board()
current_player = PLAYER_TOKEN
while True:
    print_board(board)
    if current_player == PLAYER_TOKEN:
        column = player_move(board)
    else:
        column = computer_move(board)
    drop_piece(board, column, current_player)
    if check_win(board, current_player):
        print_board(board)
        print("Победил игрок" if current_player == PLAYER_TOKEN else "Победил компьютер!")
        break
    elif all(cell != minus for row in board for cell in row):
        print_board(board)
        print("Ничья!")
        break
    current_player = AI_TOKEN if current_player == PLAYER_TOKEN else PLAYER_TOKEN