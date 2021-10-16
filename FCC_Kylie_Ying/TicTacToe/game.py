from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # We will use a single list to rep. 3x3 board
        self.current_winner = None  # Keep track of winner

    def print_board(self):
        # Getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # If move valid, make the move (assign square to letter) and return True
        # If move invalid, return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Winner if 3 in a row anywhere; we have to check all of these
        # Checking the row first:
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Check column:
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals:
        # only if the square is an even number (0, 2, 4, 6, 8)
        # because these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # top-left to bottom-right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # bottom-right to top-left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # If all checks fail, return False
        return False


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game (the letter) or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X'  # Starting letter

    # Iterate while the game still has empty squares (we don't have to worry about winner because we'll
    # just return that which breaks the loop.
    while game.empty_squares():
        # Get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}. ")
                game.print_board()
                print('')  # Prints an empty line
            # Check if we won
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            # After we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'

        # tiny pause
        time.sleep(0.8)

    if print_game:
        print("It's a tie!")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
