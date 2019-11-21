# inspired by https://www.codementor.io/mustafakharnoub/teach-your-kids-to-build-their-own-game-with-python-1-10vphy48to

import turtle
pen = turtle.Turtle()

pen.pendown()
for side in range(3):
  pen.forward(100)
  pen.right(90)
pen.forward(100)

player = turtle.Turtle()
player.shape("circle")  # choices: arrow turtle, circle, square, triangle and classic
player.penup()

def moveRight():
  player.setx(player.xcor()+10)

def moveLeft():
  player.setx(player.xcor()-10)

def moveUp():
  player.sety(player.ycor()+10)

def moveDown():
  player.sety(player.ycor()-10)

turtle.listen()

turtle.onkey(moveRight, 'Right')
turtle.onkey(moveLeft, 'Left')
turtle.onkey(moveUp, 'Up')
turtle.onkey(moveDown, 'Down')
turtle.onkey(turtle.bye, 'q')
turtle.mainloop()
