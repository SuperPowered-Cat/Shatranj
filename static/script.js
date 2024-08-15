let board = Chessboard('board', {
    position: 'start',
    draggable: true,
    onDrop: onDrop
});

let game = new Chess();

function getBestMove() {
    const fen = game.fen();
    fetch('/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ fen: fen, difficulty: 5 }),
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').innerText = `Best Move: ${data.best_move}`;
            game.move(data.best_move);
            board.position(game.fen());
        });
}

function onDrop(source, target) {
    let move = game.move({
        from: source,
        to: target,
        promotion: 'q' // Promote to queen
    });

    if (move === null) return 'snapback';

    board.position(game.fen());
}


