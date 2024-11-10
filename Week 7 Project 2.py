def load_file(filename):
    """Reads the file and returns a list of lines."""
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None

def display_line(lines, line_number):
    """Displays the requested line if the line number is valid."""
    if 1 <= line_number <= len(lines):
        print(f"Line {line_number}: {lines[line_number - 1].strip()}")
    else:
        print(f"Invalid line number. Please enter a number between 1 and {len(lines)}.")

def main():
    """Main function to navigate through file lines."""
    filename = input("Enter the filename: ")
    lines = load_file(filename)

    if lines is None:
        return

    total_lines = len(lines)
    print(f"The file contains {total_lines} lines.")

    while True:
        try:
            line_number = int(input("Enter a line number (0 to quit): "))
            if line_number == 0:
                print("Exiting the program.")
                break
            display_line(lines, line_number)
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
