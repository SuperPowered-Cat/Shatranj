from flask import Flask, render_template, request, jsonify
from stockfish_integration import get_best_move

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    fen = data['fen']
    difficulty = data.get('difficulty', 5)
    best_move = get_best_move(fen, difficulty)
    return jsonify({'best_move': str(best_move)})


if __name__ == "__main__":
    app.run(debug=True)
