initial_height = float(input("Enter the initial height from which the ball is dropped (in feet): "))
bounciness_index = float(input("Enter the bounciness index of the ball: "))
num_bounces = int(input("Enter the number of bounces allowed: "))

total_distance = initial_height

current_height = initial_height * bounciness_index

for bounce in range(1, num_bounces + 1):
    
    total_distance += 2 * current_height
    
    current_height *= bounciness_index

print(f"Total distance traveled by the ball: {total_distance:.2f} feet")
