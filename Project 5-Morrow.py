def compute_cuboid_volume():
    
    height = float(input("Enter the height of the cuboid: "))
    width = float(input("Enter the width of the cuboid: "))
    depth = float(input("Enter the depth of the cuboid: "))


    volume = height * width * depth


    print(f"The volume of the cuboid is: {volume} cubic units")

if __name__ == "__main__":
    compute_cuboid_volume()