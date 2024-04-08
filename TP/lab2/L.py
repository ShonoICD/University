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

tl.speed(0) 
tl.penup()
tl.setx(-500)
tl.sety(0)
tl.pendown()

depth = 3
way_l = l_sys('F', depth)
for i in way_l:
    if i == '-':
        tl.left(90)
    elif i == '+':
        tl.right(90)
    else:
        tl.forward(10)
tl.done()