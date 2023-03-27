def get_user_input():
    return input('Enter a number: ')

def main():
    numbers = {
        "1": "one ",
        "2": "two ",
        "3": "three ",
        "4": "four ",
        "5": "five ",
        "6": "six ",
        "7": "seven ", 
        "8": "eight ",
        "9": "nine ",
        "0": "zero "
    }
    number = get_user_input()
    output_string = ''
    for digit in number:
        output_string += (numbers[digit])
    print(output_string)    
        
if __name__ == "__main__":
    main()