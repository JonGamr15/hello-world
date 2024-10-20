try:
    
    edge_length = int(input("Enter the length of an edge of the cube: "))
    
   
    if edge_length <= 0:
        print("Edge length must be a positive integer.")
    else:
        
        surface_area = 6 * (edge_length ** 2)
        
       
        print(f"The surface area of the cube is: {surface_area} square units.")
except ValueError:
    print("Please enter a valid integer.")
