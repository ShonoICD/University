import turtle as tl

def l_sys(level, n):
    for j in range(n):
        newlevel = ''
        for i in level:
            if i == 'F':
                newlevel = newlevel + 'F-F+F+FF-F-F+F'
            elif i == '-':
                newlevel = newlevel + '-'
            elif i == '+':
                newlevel = newlevel + '+'
        level = newlevel
        # print(level)
    return level

def mino(length, depth):
    if depth == 0:
        tl.forward(length)
    else:
        mino(length / 4, depth - 1)
        tl.left(90)
        mino(length / 4, depth - 1)
        tl.right(90)
        mino(length / 4, depth - 1)
        tl.right(90)
        mino(length / 4, depth - 1)
        mino(length / 4, depth - 1)
        tl.left(90)
        mino(length / 4, depth - 1)
        tl.left(90)
        mino(length / 4, depth - 1)
        tl.right(90)
        mino(length / 4, depth - 1)

length = 200
depth = 1

print("Рекурсия - 1\nL-system - 2\nВыход - 3")

while True:
    choice = int(input())
    match choice:
        case 1:
            tl.speed(0) 
            tl.penup()
            tl.setx(-500)
            tl.sety(0)
            tl.pendown()
            mino(length, depth)
            tl.reset
        case 2:
            tl.speed(0) 
            tl.penup()
            tl.setx(-500)
            tl.sety(0)
            tl.pendown()

            way_l = l_sys('F', depth)
            for i in way_l:
                if i == '-':
                    tl.left(90)
                elif i == '+':
                    tl.right(90)
                else:
                    tl.forward(10)
            tl.reset
        case 3:
            exit()