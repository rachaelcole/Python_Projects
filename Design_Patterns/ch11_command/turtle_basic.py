
# The turtle module in the Python standard library lets us handle commands like move forward, turn left, etc.:

import turtle


turtle.setup(400, 400)

screen = turtle.Screen()
screen.title('Keyboard drawing!')

t = turtle.Turtle()
distance = 10

def advance():
    t.forward(distance)

def turn_left():
    t.left(distance)

def turn_right():
    t.right(distance)

def retreat():
    t.backward(distance)

def quit():
    screen.bye()


screen.onkey(advance, 'w')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(retreat, 's')
screen.onkey(quit, 'Escape')

screen.listen()
screen.mainloop()



# Reference: 
# Badenhurst, Wessel. "Chapter 11: Command Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 167-177,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_11.