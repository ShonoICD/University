import turtle as tl
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

length = 2000
depth = 5
tl.speed(0) 
tl.penup()
tl.setx(-500)
tl.sety(0)
tl.pendown()
mino(length, depth)
tl.done()