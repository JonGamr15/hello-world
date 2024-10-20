starting_salary = float(input("Enter the starting salary: "))
percentage_increase = float(input("Enter the percentage increase (as a whole number): ")) / 100
number_of_years = int(input("Enter the number of years for the salary schedule: "))

print(f"\n{'Year':<10}{'Salary':<15}")
print("-" * 25)

current_salary = starting_salary
for year in range(1, number_of_years + 1):
    print(f"{year:<10}{current_salary:,.2f}")
    current_salary += current_salary * percentage_increase
