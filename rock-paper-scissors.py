"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using 
input), compare them, print out a message of congratulations to the winner, and ask
if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
import random

def get_number_of_players():
    return int(input('Number of players (0-2)? '))

def get_user_input():
    choice = input('(R)ock, (P)aper, (S)cissors: ').upper()
    if choice not in ['R', 'P', 'S']:
        print('Invalid entry! Try again...')
        get_user_input()
    return choice

def determine_winner(p1_input, p2_input):
    if p1_input == 'R' and p2_input == 'R':
        return 'NOBODY'
    elif p1_input == 'R' and p2_input == 'S':
        return 'PLAYER 1'
    elif p1_input == 'R' and p2_input == 'P':
        return 'PLAYER 2'
    elif p1_input == 'P' and p2_input == 'R':
        return 'PLAYER 1'
    elif p1_input == 'P' and p2_input == 'P':
        return 'NOBODY' 
    elif p1_input == 'P' and p2_input == 'S':
        return 'PLAYER 2'
    elif p1_input == 'S' and p2_input == 'R':
        return 'PLAYER 2'
    elif p1_input == 'S' and p2_input == 'P':
        return 'PLAYER 1'
    elif p1_input == 'S' and p2_input == 'S':
        return 'NOBODY'

def main():
    play_again = True
    play_options = ['R', 'P', 'S']
    number_of_players = get_number_of_players()
    
    if number_of_players == 0:
        is_player1_cpu = True
        is_player2_cpu = True
    elif number_of_players == 1:
        is_player1_cpu = False
        is_player2_cpu = True
    elif number_of_players == 2:
        is_player1_cpu = False
        is_player2_cpu = False
    else:
        print('Enter a number between 0-2!')

    while play_again == True:
        if is_player1_cpu == False:
            print("Player 1's Turn!")
            player1_choice = get_user_input()
        else:
            player1_choice = random.choice(play_options)
            if player1_choice == 'R':
                choice_text = 'Rock'
            elif player1_choice == 'P':
                choice_text = 'Paper'
            else:
                choice_text = 'Scissors'
            print(f'Player 1 (bot) chooses {choice_text}')

        if is_player2_cpu == False:
            print("Player 2's Turn!")
            player2_choice = get_user_input()
        else:
            player2_choice = random.choice(play_options)
            if player2_choice == 'R':
                choice_text = 'Rock'
            elif player2_choice == 'P':
                choice_text = 'Paper'
            else:
                choice_text = 'Scissors'
            print(f'Player 2 (bot) chooses {choice_text}')

        print(f'The winner is {determine_winner(player1_choice, player2_choice)}')

        continue_choice = input('Play again (Y/N)? ').upper()
        if continue_choice == 'Y':
            play_again = True
        else:
            play_again = False
           
if __name__ == "__main__":
    main()
