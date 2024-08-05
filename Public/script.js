$(document).ready(function () {
    var game = new Chess();

    var board = Chessboard('board', {
        position: 'start',
        draggable: true,
        dropOffBoard: 'snapback',
        sparePieces: false,
        onDrop: function (source, target) {
            // See if the move is legal
            var move = game.move({
                from: source,
                to: target,
                promotion: 'q' // NOTE: always promote to a queen for simplicity
            });

            // Illegal move
            if (move === null) return 'snapback';

            // Make a random legal move for the opponent
            window.setTimeout(makeRandomMove, 250);
        }
    });

    function makeRandomMove() {
        var possibleMoves = game.moves();

        // Exit if the game is over
        if (game.game_over() || possibleMoves.length === 0) return;

        var randomIdx = Math.floor(Math.random() * possibleMoves.length);
        game.move(possibleMoves[randomIdx]);
        board.position(game.fen());
    }
});
