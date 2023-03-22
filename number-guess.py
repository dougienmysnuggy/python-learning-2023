import random

keep_playing = True

while keep_playing == True:
    secret_number = random.randint(1, 9)
    number_guessed = False
    guess_count = 0
    while number_guessed == False:
        user_guess = int(input('Guess a number between 1-9: ' ))
        if user_guess == secret_number:
            print('Congrats! YOU WIN!!')
            number_guessed = True
        elif user_guess < secret_number:
            print('Too Low, try again')
        else:
            print('Too High, try again')
        guess_count += 1
    print(f'It took {guess_count} guesses to get the correct answer.')
    keep_playing_choice = input('Keep playing? (Y/N): ').upper()
    if keep_playing_choice[0] == 'N':
        keep_playing = False
    else:
        keep_playing = True
