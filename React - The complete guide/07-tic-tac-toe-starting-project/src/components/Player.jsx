import {useState} from "react";


export default function Player({initialPlayerName, symbol, isActive, onPlayerNameChange}) {
    const [isEditing, setIsEditing] = useState(false)
    const [playerName, setPlayerName] = useState(initialPlayerName)

    const handleEditClick = () => {
        setIsEditing(editing => !editing)
        if (isEditing) {
            onPlayerNameChange(symbol, playerName)
        }
    }

    const handleChangePlayerName = (event) => {
        setPlayerName(_ => event.target.value)

    }

    return (
        <li className={isActive ? "active" : undefined}>
            <span className="player">
                {isEditing && <input value={playerName} type="text" required onChange={handleChangePlayerName}/>}
                {!isEditing && <span className="player-name">{playerName}</span>}

                <span className="player-symbol">{symbol}</span>
            </span>
            <button onClick={handleEditClick}>{isEditing ? "Save" : "Edit"}</button>
        </li>
    )
}