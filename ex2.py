weight = input('Enter your weight (lbs): ')
choice = input('(L)bs or (K)ilos?: ')
if choice.upper() == "L":
    converted_weight = int(weight) * 0.45
    print(f'Your weight in Kilograms is {converted_weight}.')
elif choice.upper() == "K":
    converted_weight = int(weight) / 0.45
    print(f'Your weight in Pounds is {converted_weight}.')
else:
    print('Invalid input. Try again!')