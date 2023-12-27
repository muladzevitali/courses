export default function UserInputComponent({userInput, onUserInput}) {

    return (<section id="user-input">
        <div className="input-group">
            <p>
                <label>Initial investment</label>
                <input type="number"
                       required
                       value={userInput.initialInvestment}
                       onChange={(event) => onUserInput("initialInvestment", event.target.value)}
                />
            </p>
            <p>
                <label>Annual investment</label>
                <input type="number"
                       required
                       value={userInput.annualInvestment}
                       onChange={(event) => onUserInput("annualInvestment", event.target.value)}
                />
            </p>
        </div>

        <div className="input-group">
            <p>
                <label>Expected return</label>
                <input type="number"
                       required
                       value={userInput.expectedReturn}
                       onChange={(event) => onUserInput("expectedReturn", event.target.value)}
                />
            </p>
            <p>
                <label>Duration</label>
                <input type="number"
                       required
                       value={userInput.duration}
                       onChange={(event) => onUserInput("duration", event.target.value)}
                />
            </p>
        </div>
    </section>)
}