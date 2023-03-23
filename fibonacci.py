def get_user_input():
    return int(input('Enter number of Fibonacci numbers to show: '))

def get_next_number(fib):
    return fib[len(fib) - 2] + fib[len(fib) - 1]

def main():
    total_numbers = get_user_input()
    fibonacci = [1, 1]
    while len(fibonacci) < total_numbers:
        fibonacci.append(get_next_number(fibonacci))
    print(fibonacci)

if __name__ == "__main__":
    main()