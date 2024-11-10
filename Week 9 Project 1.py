import turtle
import math

def drawCircle(t, x, y, radius):
    """Draws a circle with the specified center (x, y) and radius."""
   
    t.penup()
    t.goto(x, y - radius)  
    t.pendown()
    
    
    distance = 2.0 * math.pi * radius / 120.0
    
    
    for _ in range(120):
        t.forward(distance)
        t.left(3)  


if __name__ == "__main__":
    
    t = turtle.Turtle()
    t.speed(0)  
    
    drawCircle(t, 0, 0, 100)
    
    turtle.done()
