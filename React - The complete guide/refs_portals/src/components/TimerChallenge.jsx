import {useRef, useState} from "react";
import ResultModal from "./ResultModal";

export default function TimerChallenge({title, targetTime}) {
    const timer = useRef()
    const dialog = useRef()

    const [timeRemaining, setTimeRemaining] = useState(targetTime * 1000);

    const handleReset = () => {
        setTimeRemaining(_ => targetTime * 1000);
    }

    const handleStart = () => {
        timer.current = setInterval(() => {
            setTimeRemaining(prev => prev - 10)
        }, 10)
    }

    const handleStop = () => {
        clearInterval(timer.current)
        dialog.current.open()
    }

    const timerIsActive = timeRemaining > 0 && timeRemaining < targetTime * 1000
    if (timeRemaining < 0) {
        handleStop()
    }
    return (
        <>
            {<ResultModal ref={dialog}
                          targetTime={targetTime}
                          remainingTime={timeRemaining}
                          onReset={handleReset}
            />}
            <section className="challenge">
                <h2>{title}</h2>
                <p className="challenge-time">
                    {targetTime} second{targetTime > 1 ? "s" : ""}
                </p>
                <p>
                    <button onClick={timerIsActive ? handleStop : handleStart}>
                        {timerIsActive ? "Stop" : "Start"} Challenge
                    </button>
                </p>
                <p className={timerIsActive ? "active" : undefined}>
                    {timerIsActive ? "Time is running..." : "Timer inactive"}
                </p>
            </section>
        </>
    )
}