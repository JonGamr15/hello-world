initial_population = int(input("Enter the initial number of organisms: "))
growth_rate = float(input("Enter the growth rate (e.g., 2 for doubling): "))
growth_period = float(input("Enter the number of hours to achieve this growth rate: "))
total_hours = float(input("Enter the total number of hours the population will grow: "))

num_growth_cycles = total_hours // growth_period

total_population = initial_population * (growth_rate ** num_growth_cycles)

print(f"After {total_hours} hours, the total population is predicted to be {int(total_population)} organisms.")
