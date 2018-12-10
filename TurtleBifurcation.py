#DMM - lets create a tree!!!
import turtle as turt

#set the turtle to fastest, (we don't have time for games :P )
turt.speed('fastest')

#Draw the initial Line
turt.colormode(255)
turt.left(90)
turt.penup()
turt.backward(100)
turt.pendown()
turt.forward(100)

#In this function, d is the distance the turtle will draw the line
#a is the angle which the split will occur
#n is the number of times you want the drawSplit function to call itself
def drawSplit(d, a, n, r, g, b, p):
    turt.pencolor(r,g,b)
    #move halfway to the left, move forward d and draw a split
    turt.left(a/2)
    turt.forward(d)
    if n > 0:
        drawSplit(d * 0.8, a, n - 1, (r+p)%255, (g+2*p)%255, (b+3*p)%255, p)
    
    #Move back, turn to the right d, and draw another split
    turt.pencolor(r,g,b)
    turt.backward(d)
    turt.right(a)
    turt.forward(d)
    if n > 0:
        drawSplit(d * 0.8, a, n - 1, (r+p)%255, (g+2*p)%255, (b+3*p)%255, p)

    #Move back and face where you started
    turt.pencolor(r,g,b)
    turt.backward(d)
    turt.left(a/2)

#start drawing the splits
drawSplit(90, 26, 10, 3, 130, 255, 5)

#hold the screen open util the user clicks it
turt.exitonclick()