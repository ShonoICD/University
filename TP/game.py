import random

ROWS = 6
COLUMNS = 7

EMPTY_SLOT = '-'
PLAYER_TOKEN = 'X'
AI_TOKEN = 'O'


# cоздаем доску с помощью списка в списке
def create_board():
    return [[EMPTY_SLOT for _ in range(COLUMNS)] for _ in range(ROWS)]

# печатаем доску
def print_board(board):
    for row in board:
        print(' '.join(row))
    print('1 2 3 4 5 6 7')

# проверяем что самый верхний ряд любого столбца имеет символ '-'
def is_valid_move(board, column):
    return board[0][column] == EMPTY_SLOT

# проходим по матрице с нижней строки (то есть в обратном порядке) и когда находим символ '-' 
# в выбранном столбце то ставим туда символ в зависимости от хода (игрок или ии)
def drop_piece(board, column, token):
    for row in range(ROWS-1, -1, -1):
        if board[row][column] == EMPTY_SLOT:
            board[row][column] = token
            break
# проверяем вниз, вправо, вниз-влево, вниз-вправо
def check_win(board, token):
    for row in range(ROWS):
        for col in range(COLUMNS):
            if col + 3 < COLUMNS and all(board[row][col + i] == token for i in range(4)):
                return True
            if row + 3 < ROWS and all(board[row + i][col] == token for i in range(4)):
                return True
            if col + 3 < COLUMNS and row + 3 < ROWS and all(board[row + i][col + i] == token for i in range(4)):
                return True
            if col + 3 < COLUMNS and row - 3 >= 0 and all(board[row - i][col + i] == token for i in range(4)):
                return True
    return False

# проверка на правильно введенную позицию и если тру возвращаем номер столбца - 1
def player_move(board):
    while True:
        try:
            column = int(input("Ваш ход (введите номер столбца от 1 до 7): ")) - 1
            if 0 <= column < COLUMNS and is_valid_move(board, column):
                return column
            else:
                print("Некорректный ход. Попробуйте еще раз.")
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")
# рандомно тыкает фишки
def ai_move(board):
    available_columns = [col for col in range(COLUMNS) if is_valid_move(board, col)]
    return random.choice(available_columns)


board = create_board()
current_player = PLAYER_TOKEN

while True:
    print_board(board)
        
    if current_player == PLAYER_TOKEN:
        column = player_move(board)
    else:
        column = ai_move(board)
        
    drop_piece(board, column, current_player)
        
    if check_win(board, current_player):
        print_board(board)
        print("Победил игрок" if current_player == PLAYER_TOKEN else "Победил компьютер!")
        break
    elif all(cell != EMPTY_SLOT for row in board for cell in row):
        print_board(board)
        print("Ничья!")
        break
        
    current_player = AI_TOKEN if current_player == PLAYER_TOKEN else PLAYER_TOKEN
