hourly_wage = float(input("Enter the hourly wage: "))
regular_hours = float(input("Enter the total regular hours worked: "))
overtime_hours = float(input("Enter the total overtime hours worked: "))

regular_pay = hourly_wage * regular_hours

overtime_pay = overtime_hours * (1.5 * hourly_wage)

total_weekly_pay = regular_pay + overtime_pay

print(f"The total weekly pay is: ${total_weekly_pay:.2f}")
