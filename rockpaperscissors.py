import random

# Rock paper scissors game
# r > s, p > r, s > p

def play():
    user = input("Choose your weapon: 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won!"

    return "You lost."

# helper function
def is_win(player, opponent):
    # return True if player wins
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
            or (player == 's' and opponent == 'p'):
        return True


print(play())
