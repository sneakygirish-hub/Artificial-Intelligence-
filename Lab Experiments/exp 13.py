import math

class TicTacToeAlphaBeta:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.ai = "O"
        self.human = "X"

    def print_board(self):
        print(f"\n {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} \n")

    def check_winner(self, board):
        win_conditions = [, [3, 4, 5], [6, 7, 8],  # Horizontal Rows, [1, 4, 7], [2, 5, 8],  # Vertical Columns, [2, 4, 6]              # Diagonal Crossings
        ]
        for cond in win_conditions:
            if board[cond[0]] == board[cond[1]] == board[cond[2]] != " ":
                return board[cond[0]]
        return None

    def is_board_full(self, board):
        return " " not in board

    def minimax(self, board, depth, alpha, beta, is_maximizing):
        """Minimax algorithm optimized with Alpha-Beta Pruning."""
        winner = self.check_winner(board)
        
        # Base Cases: Return evaluation scores
        if winner == self.ai:
            return 10 - depth  # Fast wins score higher
        if winner == self.human:
            return depth - 10  # Prolonged losses score better
        if self.is_board_full(board):
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if board[i] == " ":
                    board[i] = self.ai
                    score = self.minimax(board, depth + 1, alpha, beta, False)
                    board[i] = " "  # Undo move
                    best_score = max(score, best_score)
                    
                    # Alpha update and beta pruning condition
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break  # Prune this branch
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == " ":
                    board[i] = self.human
                    score = self.minimax(board, depth + 1, alpha, beta, True)
                    board[i] = " "  # Undo move
                    best_score = min(score, best_score)
                    
                    # Beta update and alpha pruning condition
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break  # Prune this branch
            return best_score

    def find_best_move(self):
        """Finds the perfect move position for the AI using Alpha-Beta search values."""
        best_score = -math.inf
        move = -1
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = self.ai
                # Initial alpha = -infinity, beta = +infinity
                score = self.minimax(self.board, 0, -math.inf, math.inf, False)
                self.board[i] = " "  # Undo move
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def play(self):
        print("=" * 40)
        print("  TIC-TAC-TOE VS OPTIMIZED ALPHA-BETA AI")
        print("=" * 40)
        print("Positions are indexed from 1 to 9 (Top-left to Bottom-right).")
        
        self.print_board()

        while True:
            # Human Player Turn
            try:
                human_move = int(input("Enter your move position (1-9): ")) - 1
                if human_move < 0 or human_move > 8 or self.board[human_move] != " ":
                    print("Invalid spot! Choose an available empty position.")
                    continue
            except ValueError:
                print("Please enter a valid numerical number.")
                continue

            self.board[human_move] = self.human
            self.print_board()

            if self.check_winner(self.board) == self.human:
                print("Unbelievable! You beat the AI!")
                break
            if self.is_board_full(self.board):
                print("It's a tie draw! 🤝")
                break

            # AI Player Turn
            print("AI is calculating the optimal path...")
            ai_move = self.find_best_move()
            self.board[ai_move] = self.ai
            self.print_board()

            if self.check_winner(self.board) == self.ai:
                print("Game Over. The Alpha-Beta AI wins! 🤖")
                break
            if self.is_board_full(self.board):
                print("It's a tie draw! 🤝")
                break

if __name__ == "__main__":
    game = TicTacToeAlphaBeta()
    game.play()
