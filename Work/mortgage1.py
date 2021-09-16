principal = 5e5
rate = 5e-2
payment = 2684.11
total_paid = 0.0
i = 1

while principal > 0:

    if i <= 12:
        principal = principal * (1 + rate/12) - (payment + 1000)

        if principal < 0:
            payment = payment + principal
            
        total_paid = total_paid + payment + 1000
    else:
        principal = principal * (1 + rate/12) - payment

        if principal < 0:
            payment = payment + principal

        total_paid = total_paid + payment
    i = i + 1

print(f'Total paid is {round(total_paid, 2)} over {i-1} months')