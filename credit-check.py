PRICE = 1000000
credit_good = True

if credit_good:
    down_payment = PRICE * .10
else:
    down_payment = PRICE * .20

print(f"Down payment required: ${down_payment}")