from functools import reduce

def compute_average(filename):
    """Computes the average of the numbers in the given text file."""
    try:
        with open(filename, 'r') as file:
            # Use map to convert each line to a float
            numbers = list(map(float, file))
            
            # Use reduce to compute the sum of the numbers
            total = reduce(lambda x, y: x + y, numbers)
            
            # Calculate the average
            average = total / len(numbers) if numbers else 0
            return average
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: Ensure the file contains only numbers, one per line.")
    except ZeroDivisionError:
        print("Error: The file is empty, so the average cannot be computed.")

# Tester program
if __name__ == "__main__":
    filename = input("Enter the filename: ")
    average = compute_average(filename)
    if average is not None:
        print(f"The average of the numbers in '{filename}' is: {average}")
