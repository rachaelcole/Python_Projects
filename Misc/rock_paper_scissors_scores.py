import random

# A simple rock, paper, scissors game
# rock > scissors, paper > rock, scissors > paper
user_score = 0
computer_score = 0
games_played = 0
while True:
    user_action = input('\nEnter a choice (rock, paper, scissors): ').lower()
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)


    print(f'You chose {user_action} and the computer chose {computer_action}.')

    if user_action == computer_action:
        print("It's a draw!\n")
    elif user_action == 'rock':
        if computer_action == 'scissors':
            user_score += 1
            print('You win!\n')
        else:
            computer_score += 1
            print('Computer wins!\n')
    elif user_action == 'paper':
        if computer_action == 'rock':
            user_score += 1
            print('You win!\n')
        else:
            computer_score += 1
            print('Computer wins!\n')
    elif user_action == 'scissors':
        if computer_action == 'paper':
            user_score += 1
            print('You win!\n')
        else:
            computer_score += 1
            print('Computer wins!\n')
    games_played += 1
    print(f'Your score: {user_score}')
    print(f'Computer score: {computer_score}')
    print(f'Games played: {games_played}')
    play_again = input("Play again? y/n: ")
    if play_again.lower() != 'y':
        print('\nBye!')
        break
