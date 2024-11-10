import turtle

def drawFractalLine(t, distance, angle, level):
    """Draws a fractal line segment at a given recursion level."""
    if level == 0:
        
        t.forward(distance)
    else:
        
        distance /= 3  
        
        
        drawFractalLine(t, distance, angle, level - 1)  
        t.left(60)  "
        drawFractalLine(t, distance, angle, level - 1)  
        t.right(120)  
        drawFractalLine(t, distance, angle, level - 1)  
        t.left(60)  
        drawFractalLine(t, distance, angle, level - 1)
        
def drawKochSnowflake(t, distance, level):
    """Draws the full Koch snowflake by drawing three fractal lines."""
    angles = [0, -120, 120] 
    for angle in angles:
        t.setheading(angle) 
        drawFractalLine(t, distance, angle, level)  

t = turtle.Turtle()
t.speed(0)  
turtle.setup(width=800, height=800)
t.penup()
t.goto(-200, 100)  
t.pendown()


drawKochSnowflake(t, 300, 2)


turtle.done()
