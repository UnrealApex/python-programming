import turtle
import time

# draw a 100 x 100 pixel square(takes parameter size which is 100 if the no argument is given)
def draw_square(size=100):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
# make four squares
for i in range(4):
    # draw a square
    draw_square()
    # turn right to drawn another square
    turtle.right(90)
# keep the window open for 5 seconds after the loop is done executing so we can view the output
time.sleep(5)

