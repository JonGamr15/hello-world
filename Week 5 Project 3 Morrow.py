import math

lower_bound = int(input("Enter the lower bound of the number you're thinking of: "))
upper_bound = int(input("Enter the upper bound of the number you're thinking of: "))


if lower_bound >= upper_bound:
    print("Invalid bounds. The lower bound must be less than the upper bound.")
else:

    min_guesses = math.ceil(math.log(upper_bound - lower_bound + 1, 2))
    print(f"The computer will try to guess your number in a maximum of {min_guesses} tries.")

    attempts = 0
    guess = None

    while True:
        
        guess = (lower_bound + upper_bound) // 2
        attempts += 1

        print(f"Computer guesses: {guess}")
        response = input("Is the guess (c)orrect, (h)igh, or (l)ow? ").lower()

        if response == 'c':
            print(f"Computer guessed your number {guess} in {attempts} attempts!")
            break
        elif response == 'h':
            upper_bound = guess - 1
        elif response == 'l':
            lower_bound = guess + 1
        else:
            print("Invalid response. Please enter 'c', 'h', or 'l'.")

        
        if lower_bound > upper_bound:
            print("Inconsistent hints provided. Please ensure your hints are correct.")
            break
