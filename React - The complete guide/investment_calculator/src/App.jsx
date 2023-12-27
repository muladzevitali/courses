import Header from "./components/Header";
import UserInputComponent from "./components/UserInputComponent";
import Results from "./components/Results";
import {useState} from "react";

function App() {
    const [userInput, setUserInput] = useState({
        initialInvestment: 10000, annualInvestment: 1200, expectedReturn: 6, duration: 10
    });

    const isInputValid = userInput.duration > 0
    const handleUserInput = (inputIdentifier, newValue) => {
        setUserInput(prevState => {
            return {...prevState, [inputIdentifier]: +newValue}
        })
    }

    return (
        <>
            <Header/>
            <UserInputComponent userInput={userInput} onUserInput={handleUserInput}/>
            {isInputValid && <Results userInput={userInput} />}
            {!isInputValid && <p className="center">Input is not valid</p>}

        </>
    )
}

export default App
