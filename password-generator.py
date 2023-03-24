"""
Password generator for PracticePython.com

easy uses 8 characters, only letters
mid uses 12 characters, letters & numbers
hard uses 16 characters, letters, numbers, & symbols
"""

import string
import random

def get_user_input():
    return input('Password Strength? (E)asy, (M)id, (H)ard: ').lower()

def generate_password(digits, choices):
    password = []
    for i in range(digits):
        password.append(random.choice(choices))
    return ''.join(password)

def main():
    choice = ''
    while choice not in ['e', 'm', 'h']:
        choice = get_user_input()
        if choice == "e":
            char_choices = list(string.ascii_letters)
            generated_password = generate_password(8, char_choices)
        elif choice == "m":
            char_choices = list(string.ascii_letters + string.digits)
            generated_password = generate_password(12, char_choices)
        elif choice == "h":
            char_choices = list(string.ascii_letters + string.punctuation + string.digits)
            generated_password = generate_password(16, char_choices)
        else:
            print('Invalid input. Try again.')

    print(generated_password)

if __name__ == "__main__":
    main()