import math
import random

class Player:
    def __init__(self, letter):
        # Letter is x or o
        self.letter = letter

    # We want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # We are going to check that this is a correct value by trying to cast it to an integer, and
            # if it's not, then we say its invalid. If that spot is not available on the board, we also say
            # its invalid.
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square= True
            except ValueError:
                print("Invalid square. Try again.")
        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # Randomly chooses a square
        else:
            # Get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'  # the other player; whatever letter is not player

        # First we want to check if the previous move is a winner
        # This is our base case
        if state.current_winner == other_player:
            # We should return position and score because we need to keep track of the score for minimax to work
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():  # No empty squares
            return {'position': None, 'score': 0}

        # Initialise some dictionaries
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximise (be larger)
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimise (be smaller)

        for possible_move in state.available_moves():
            # Step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # Step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)  # now, we alternate players
            # Step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # Otherwise this will get messed up from recursion
            # Step 4: update dictionaries if necessary
            if player == max_player:  # trying to maximise the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score  # replace best
            else:  # but minimise the other player
                if sim_score['score'] < best['score']:
                    best = sim_score  # replace best
        return best
