def get_number():
    return int(input('Enter a number: '))

def check_divisors(num):
    num_divisors = 0
    for i in range(2, (num // 2 + 1)):
        if num % i == 0:
            num_divisors += 1
    return num_divisors

def main():
    is_prime = False
    user_number = get_number()
    if check_divisors(user_number) == 0:
        print(f'{user_number} is a prime number. ')
    else:
        print(f'{user_number} is NOT a prime number. ')


if __name__ == "__main__":
    main()