principal = 5e5
rate = 5e-2
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1 + rate/12) - payment

    if principal < 0:
        payment = payment + principal

    total_paid = total_paid + payment

print('Total paid is', round(total_paid, 2))