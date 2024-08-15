import chess
import chess.engine

STOCKFISH_PATH = "C:/Users/KIIT/Shatranj/new/shatranj_env/shatranj-ai/stockfish-windows-x86-64-avx2.exe"


def play_game():
    board = chess.Board()

    with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
        while not board.is_game_over():
            print(board)
            user_move = input("Enter your move: ")

            # Validate and make the player's move
            try:
                move = chess.Move.from_uci(user_move)
                if move in board.legal_moves:
                    board.push(move)
                else:
                    print("Illegal move! Try again.")
                    continue
            except ValueError:
                print("Invalid move format! Use UCI notation (e.g., e2e4).")
                continue

            # Get the bot's move
            result = engine.play(board, chess.engine.Limit(time=2.0))
            board.push(result.move)
            print(f"Stockfish move: {result.move}\n")

        print("Game over!")
        print(board.result())


def get_best_move(fen, difficulty=1):
    # Initialize the Stockfish engine
    with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
        # Set difficulty level (Skill Level ranges from 0 to 20)
        engine.configure({"Skill Level": difficulty})

        # Create a board from the FEN string
        board = chess.Board(fen)

        # Get the best move
        result = engine.play(board, chess.engine.Limit(time=2.0))

        return result.move


if __name__ == "__main__":
    play_game()
