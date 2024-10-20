import math


try:
    radius = float(input("Enter the radius of the sphere: "))

    
    if radius <= 0:
        print("Radius must be a positive number.")
    else:
    
        diameter = 2 * radius
        
    
        circumference = 2 * math.pi * radius
        
        
        surface_area = 4 * math.pi * (radius ** 2)


        volume = (4 / 3) * math.pi * (radius ** 3)
        
        
        print(f"Diameter: {diameter:.2f} units")
        print(f"Circumference: {circumference:.2f} units")
        print(f"Surface Area: {surface_area:.2f} square units")
        print(f"Volume: {volume:.2f} cubic units")
except ValueError:
    print("Please enter a valid number.")
