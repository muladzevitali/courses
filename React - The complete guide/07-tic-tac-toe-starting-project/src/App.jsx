import Player from "./components/Player.jsx";
import GameBoard from "./components/GameBoard.jsx";
import {useState} from "react";
import Log from "./components/Log";
import {WINNING_COMBINATIONS} from "./winning-combinations.js";
import GameOver from "./components/GameOver.jsx";

const INITIAL_GAME_BOARD = [
    [null, null, null],
    [null, null, null],
    [null, null, null]
]

const PLAYERS = {X: "Player 1", O: "Player 2"}

const deriveActivePlayer = gameTurns => {
    let activePlayer = "X";

    if (gameTurns.length > 0 && gameTurns[0].player === "X") {
        activePlayer = "O"
    }

    return activePlayer
}

const deriveWinner = board => {
    for (const combination of WINNING_COMBINATIONS) {
        const firstSquareSymbol = board[combination[0].row][combination[0].column]
        const secondSquareSymbol = board[combination[1].row][combination[1].column]
        const thirdSquareSymbol = board[combination[2].row][combination[2].column]

        if (firstSquareSymbol && firstSquareSymbol === secondSquareSymbol && firstSquareSymbol === thirdSquareSymbol) {
            return firstSquareSymbol;
        }
    }

    return undefined
}

const deriveGameBoard = turns => {
    let gameBoard = [...INITIAL_GAME_BOARD.map(array => [...array])];
    for (const turn of turns) {
        const {square, player} = turn
        const {row, col} = square

        gameBoard[row][col] = player;
    }

    return gameBoard
}


function App() {
    const [gameTurns, setGameTurns] = useState([])
    const [players, setPlayers] = useState(PLAYERS)

    const activePlayer = deriveActivePlayer(gameTurns)
    let gameBoard = deriveGameBoard(gameTurns)

    let winnerSymbol = deriveWinner(gameBoard)
    let winner = players[winnerSymbol]

    const hasDraw = gameTurns.length === 9 && !winner

    const handleSelectSquare = (rowIndex, colIndex) => {
        setGameTurns(prevTurns => {
            const currentPlayer = deriveActivePlayer(prevTurns)

            return [
                {square: {row: rowIndex, col: colIndex}, player: currentPlayer},
                ...prevTurns
            ]
        })
    }

    const handleRematch = () => {
        setGameTurns([]);
    }

    const handlePlayerNameChange = (symbol, playerName) => {
        setPlayers(prevState => ({...prevState, [symbol]: playerName}))
    }

    return (<main>
        <div id="game-container">
            <ol id="players" className="highlight-player">
                <Player
                    initialPlayerName={PLAYERS.X}
                    symbol="X"
                    isActive={activePlayer === "X"}
                    onPlayerNameChange={handlePlayerNameChange}
                />
                <Player
                    initialPlayerName={PLAYERS.O}
                    symbol="O"
                    isActive={activePlayer === "O"}
                    onPlayerNameChange={handlePlayerNameChange}
                />
            </ol>
            {(winner || hasDraw) && <GameOver winner={winner} onRematch={handleRematch}/>}
            <GameBoard
                onSelectSquare={handleSelectSquare}
                board={gameBoard}
            />
        </div>
        <Log turns={gameTurns}/>
    </main>)
}

export default App
