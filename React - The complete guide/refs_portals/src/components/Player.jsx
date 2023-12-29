import {useRef, useState} from "react";

export default function Player() {
    const playerName = useRef();

    const [enteredPlayerName, setEnteredPlayerName] = useState("")

    const handleClick = () => {
        setEnteredPlayerName(_ => playerName.current.value);

    }

    return (
        <section id="player">
            <h2>Welcome {enteredPlayerName ?? "unknown entity"} </h2>
            <p>
                <input type="text"
                       ref={playerName}
                />
                <button onClick={handleClick}>Set Name</button>
            </p>
        </section>
    );
}
