# importing turtle for graphics
import turtle

# Forming the window screen
tut = turtle.Screen()

# background color white
tut.bgcolor("white")

colors = ['red', 'orange','yellow', 'pink', 'violet', 'blue']

# object
pen = turtle.Turtle()

#speed of pen
pen.speed(500)

# pen colour
pen.fillcolor("black")

# object width
pen.width(20)

# Set position of pointer
pen.setpos(0,-100)
 
# start the filling color
pen.begin_fill()
  
# drawing the circle of radius r
pen.circle(100)
  
# ending the filling of the color
pen.end_fill()

# Reset position of pointer
pen.setpos(0,0)

# Drawing web
for x in range(110):
    pen.pencolor(colors[x%6]) # switching colours
    pen.width(x/1000 + 1) # setting width
    pen.forward(x) # moving forward
    pen.left(59) # moving left

# Reset position of pointer
turtle.setpos(0,-70)

turtle.color("white smoke")

# Writing text
turtle.write("M",align='center',font=("courier",100,"bold"))

turtle.done()


