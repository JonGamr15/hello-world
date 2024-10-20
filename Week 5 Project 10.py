
down_payment_percentage = 0.10
annual_interest_rate = 0.12
monthly_payment_percentage = 0.05

purchase_price = float(input("Enter the purchase price: "))

down_payment = purchase_price * down_payment_percentage

loan_amount = purchase_price - down_payment

monthly_payment = monthly_payment_percentage * purchase_price

current_balance = loan_amount
month_number = 0


print(f"{'Month':<10}{'Total Balance':<20}{'Interest Owed':<20}{'Principal Owed':<20}{'Payment':<20}{'Remaining Balance':<20}")
print("-" * 110)


while current_balance > 0:
    month_number += 1
    interest_owed = current_balance * (annual_interest_rate / 12)
    principal_owed = monthly_payment - interest_owed
    
    if principal_owed > current_balance:
        principal_owed = current_balance
    
    
    remaining_balance = current_balance - principal_owed
    
    print(f"{month_number:<10}{current_balance:<20.2f}{interest_owed:<20.2f}{principal_owed:<20.2f}{monthly_payment:<20.2f}{remaining_balance:<20.2f}")
    
    current_balance = remaining_balance
