import random
import sys

print('ROCK, PAPER, SCISSORS')

# Initialise vars to keep track of wins, losses and ties
wins = 0
losses = 0
ties = 0

while True:     # the main game loop
    print(f'{wins} Wins | {losses} Losses | {ties} Ties')

    while True:     # the player input loop
        print('Enter your move: (r)ock, (p)aper, or (s)cissors? (press \'q\' to quit)')
        player_move = input().lower()
        if player_move == 'q':
            sys.exit()   # Quit the program
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break       # break out of the player input loop
        print('Type one of r, p, s, or q')

    # Display what the player chose
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 's':
        print('SCISSORS versus...')
    else:
        print('PAPER versus...')

    # Display what the computer chose
    random_num = random.randint(1, 3)
    if random_num == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_num == 2:
        computer_move = 's'
        print('SCISSORS')
    else:
        computer_move = 'p'
        print('PAPER')

    # DEBUGGING
    # print(f'\nDEBUG: random_num is {random_num}')
    # print(f'DEBUG: computer_move is {computer_move}')
    # print(f'DEBUG: player_move is {player_move}\n')


    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print('It\'s a tie!')
        ties += 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins += 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins += 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins += 1
    elif player_move == 'r' and computer_move == 'p':
        print('Computer wins!')
        losses += 1
    elif player_move == 's' and computer_move == 'r':
        print('Computer wins!')
        losses += 1
    elif player_move == 'p' and computer_move == 's':
        print('Computer wins!')
        losses += 1
