
# new years eve project lol
# trying to draw with color

import turtle

t = turtle.Turtle()

t.speed(10)

t.pensize(2)

t.shape('turtle')

# the road
t.fillcolor('#D3D3D3')

t.begin_fill()
t.right(45)
t.forward(283)
t.right(135)
t.forward(400)
t.right(135)
t.forward(283)
t.end_fill()

# road lines

t.penup()
t.goto(0,-3)
t.right(45)
t.pendown()
t.pensize(2)
t.fillcolor('white')

#first dash
t.begin_fill()
t.right(60)
t.forward(20)
t.right(120)
t.forward(20)
t.right(120)
t.forward(20)
t.end_fill()

t.penup()
t.back(20)
t.setheading(90)
t.back(10)

#second dash
t.begin_fill()
t.pendown()
t.right(90)
t.forward(20)
t.right(60)
t.forward(25)
t.right(120)
t.forward(45)
t.right(120)
t.forward(25)
t.end_fill()

t.penup()
t.back(25)
t.setheading(90)
t.back(15)

#third dash
t.begin_fill()
t.pendown()
t.right(90)
t.forward(45)
t.right(60)
t.forward(35)
t.right(120)
t.forward(80)
t.right(120)
t.forward(35)
t.end_fill()

t.penup()
t.back(35)
t.setheading(90)
t.back(20)

#fourth dash
t.begin_fill()
t.pendown()
t.right(90)
t.forward(80)
t.right(60)
t.forward(50)
t.right(120)
t.forward(130)
t.right(120)
t.forward(50)
t.end_fill()

#positioning to begin buildings
t.penup()
t.goto(0,0)
t.setheading(0)
t.right(45)

#first right building
t.forward(10)
t.setheading(90)
t.pendown()

t.fillcolor('#C1E1C1')
t.begin_fill()
t.forward(30)
t.right(45)
t.forward(15)
t.setheading(270)
t.forward(51)
t.end_fill()

t.fillcolor('#556b2f')
t.begin_fill()
t.penup()
t.back(51)
t.setheading(0)
t.pendown()
t.forward(20)
t.setheading(270)
t.forward(51)
t.setheading(180)
t.forward(20)
t.end_fill()



#positioning to begin buildings
t.penup()
t.goto(0,0)
t.setheading(0)
t.right(45)

#second right building
t.forward(54)
t.setheading(90)
t.pendown()

t.fillcolor('#F8C8DC')
t.begin_fill()
t.forward(100)
t.right(45)
t.forward(40)
t.setheading(270)
t.forward(155)
t.end_fill()

t.fillcolor('#D198B7')
t.begin_fill()
t.penup()
t.back(155)
t.setheading(0)
t.pendown()
t.forward(55)
t.setheading(270)
t.forward(155)
t.setheading(180)
t.forward(55)
t.end_fill()

#positioning to begin buildings
t.penup()
t.goto(0,0)
t.setheading(0)
t.right(45)

#third right building
t.forward(171)
t.setheading(90)
t.pendown()

t.fillcolor('#A7C7E7')
t.begin_fill()
t.forward(250)
t.right(45)
t.forward(80)
t.setheading(270)
t.forward(362)
t.end_fill()

t.fillcolor('#779ecb')
t.begin_fill()
t.penup()
t.back(362)
t.setheading(0)
t.pendown()
t.forward(100)
t.setheading(270)
t.forward(362)
t.setheading(180)
t.forward(100)
t.end_fill()

#positioning to begin buildings
t.penup()
t.goto(0,0)
t.setheading(180)
t.left(45)

#first left building
t.forward(10)
t.setheading(90)
t.pendown()

t.fillcolor('#FDFD96')
t.begin_fill()
t.forward(30)
t.left(45)
t.forward(15)
t.setheading(270)
t.forward(51)
t.end_fill()

t.fillcolor('#FDDD5C')
t.begin_fill()
t.penup()
t.back(51)
t.setheading(180)
t.pendown()
t.forward(20)
t.setheading(270)
t.forward(51)
t.setheading(0)
t.forward(20)
t.end_fill()

#positioning to begin buildings
t.penup()
t.goto(0,0)
t.setheading(180)
t.left(45)

#second left building
t.forward(54)
t.setheading(90)
t.pendown()

t.fillcolor('#E0BBE4')
t.begin_fill()
t.forward(100)
t.left(45)
t.forward(40)
t.setheading(270)
t.forward(155)
t.end_fill()

t.fillcolor('#957DAD')
t.begin_fill()
t.penup()
t.back(155)
t.setheading(180)
t.pendown()
t.forward(55)
t.setheading(270)
t.forward(155)
t.setheading(0)
t.forward(55)
t.end_fill()

#positioning to begin buildings
t.penup()
t.goto(0,0)
t.setheading(180)
t.left(45)

#third right building
t.forward(171)
t.setheading(90)
t.pendown()

t.fillcolor('#FFBEAD')
t.begin_fill()
t.forward(250)
t.left(45)
t.forward(80)
t.setheading(270)
t.forward(362)
t.end_fill()

t.fillcolor('#FFA694')
t.begin_fill()
t.penup()
t.back(362)
t.setheading(180)
t.pendown()
t.forward(100)
t.setheading(270)
t.forward(362)
t.setheading(0)
t.forward(100)
t.end_fill()


















