principal = 5e5
rate = 5e-2
payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
i = 1

while principal > 0:

    if i >= extra_payment_start_month and i <= extra_payment_end_month:
        principal = principal * (1 + rate/12) - (payment + extra_payment)

        if principal < 0:
            payment = payment + principal
            
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1 + rate/12) - payment

        if principal < 0:
            payment = payment + principal

        total_paid = total_paid + payment
    i = i + 1

print(f'Total paid is {round(total_paid, 2)} over {i-1} months')