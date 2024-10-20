
source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

try:
    
    with open(source_file, 'r') as infile:
        
        content = infile.read()

   
    with open(destination_file, 'w') as outfile:
        outfile.write(content)

    print(f"Contents of '{source_file}' have been successfully copied to '{destination_file}'.")

except FileNotFoundError:
    print(f"Error: The file '{source_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
