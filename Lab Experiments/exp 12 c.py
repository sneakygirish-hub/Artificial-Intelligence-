class TicTacToe:
    def __init__(self):
        # Represent a 3x3 board using a list of 9 single-space strings
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        """Renders the current visual grid layout."""
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")

    def print_board_guide(self):
        """Displays position index numbers for player instructions."""
        print("Grid Position Guide:")
        print(" 1 | 2 | 3 ")
        print("---+---+---")
        print(" 4 | 5 | 6 ")
        print("---+---+---")
        print(" 7 | 8 | 9 ")
        print("-" * 20)

    def check_winner(self):
        """Checks rows, columns, and diagonals for a matching three-in-a-row."""
        win_conditions = [ [3, 4, 5], [6, 7, 8],  # Horizontal Rows, [1, 4, 7], [2, 5, 8],  # Vertical Columns, [2, 4, 6]              # Diagonal Crossing Paths
        ]
        
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                return self.board[condition[0]]
        return None

    def is_board_full(self):
        """Returns True if no empty spaces remain."""
        return " " not in self.board

    def play_game(self):
        """Main game control processing loop."""
        print("=" * 30)
        print("        TIC-TAC-TOE GAME")
        print("=" * 30)
        self.print_board_guide()

        while True:
            self.print_board()
            print(f"Player '{self.current_player}' turn.")
            
            # Input parsing and constraint enforcement
            try:
                move = int(input("Select a position index (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid choice! Choose a index position value between 1 and 9.")
                    continue
                if self.board[move] != " ":
                    print("That position is already occupied! Try another cell.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a valid numerical number.")
                continue

            # Assign symbol and evaluate board configuration alterations
            self.board[move] = self.current_player
            
            winner = self.check_winner()
            if winner:
                self.print_board()
                print(f"Congratulations! Player '{winner}' has won the match! 🎉")
                break
                
            if self.is_board_full():
                self.print_board()
                print("The game ended in a tie draw! 🤝")
                break

            # Alternate current playing status tracker flag
            self.current_player = "O" if self.current_player == "X" else "X"


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
