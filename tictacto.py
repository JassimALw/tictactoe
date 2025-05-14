class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    def check_winner(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        return any(self.board[a] == self.board[b] == self.board[c] == player for a, b, c in win_conditions)
    
    def make_move(self, move):
        if self.board[move] == " ":
            self.board[move] = self.current_player
            if self.check_winner(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                return True
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")
        return False
    
    def play_game(self):
        for turn in range(9):
            self.print_board()
            move = int(input(f"Player {self.current_player}, choose your move (1-9): ")) - 1
            if self.make_move(move):
                return
        self.print_board()
        print("It's a tie!")

game = TicTacToe()
game.play_game()
