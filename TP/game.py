import os
length = 7
height = 6
table = []

def create_board():
    for i in range(height):
        table.append([0]*length)

def output(table):
    for row in table:
        for elem in row:
            print(elem, end = ' ')
        print()
    os.system('cls')

def switch_turn(turn):
    return 2 if turn == 1 else 1

def check_column(column, table):
    if table[]

print('choose your turn')
print()
turn = int(input())





