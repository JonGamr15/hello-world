try:
    
    mass = float(input("Enter the object's mass (in kilograms): "))
    
   
    velocity = float(input("Enter the object's velocity (in meters per second): "))
    
   
    if mass < 0:
        print("Mass cannot be negative.")
    elif velocity < 0:
        print("Velocity cannot be negative.")
    else:
        
        momentum = mass * velocity
        
        
        print(f"The object's momentum is: {momentum:.2f} kg·m/s")
except ValueError:
    print("Please enter a valid number.")
