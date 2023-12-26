export default function GameBoard({board, onSelectSquare}) {

    return (
        <ol id="game-board">
            {board.map((row, rowIndex) => <li key={rowIndex}>
                <ol>
                    {row.map((playerSymbol, colIndex) =>
                        <li key={colIndex}>
                            <button
                                onClick={() => onSelectSquare(rowIndex, colIndex)}
                                disabled={board[rowIndex][colIndex] !== null}
                            >
                                {playerSymbol}
                            </button>
                        </li>
                    )}
                </ol>
            </li>)}
        </ol>
    )
}