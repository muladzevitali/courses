import { View, StyleSheet, Alert, Text, FlatList } from "react-native"
import { Ionicons } from '@expo/vector-icons'
import Title from '../components/ui/Title'
import { useState, useEffect } from "react";
import InputBoundaries from "../constants/inputBoundaries";
import NumberContainer from "../components/game/NumberContainer";
import PrimaryButton from "../components/ui/PrimaryButton";
import Card from "../components/ui/Card";
import InstructionText from "../components/ui/InstructionText";
import GuessLogItem from "../components/game/GuessLogItem";


function generateRandomBetween(min, max, exclude) {
    const rndNum = Math.floor(Math.random() * (max - min)) + min;


    if (rndNum >= InputBoundaries.max + 1 || rndNum <= InputBoundaries.min - 1) {
        return rndNum
    }

    if (rndNum === exclude) {
        return generateRandomBetween(min, max, exclude);
    } else {
        return rndNum;
    }
}

let minBoundary = InputBoundaries.min
let maxBoundary = InputBoundaries.max + 1


const GameScreen = ({ enteredNumber, onGameOver }) => {
    const initialGuess = generateRandomBetween(1, 10000, enteredNumber)
    const [currentGuess, setCurrentGuess] = useState(initialGuess)
    const [guessRounds, setGuessRounds] = useState([initialGuess])

    useEffect(() => {
        if (currentGuess == enteredNumber) {
            onGameOver(guessRounds.length)
        }
    },
        [currentGuess, enteredNumber, onGameOver]
    )

    useEffect(() => {
        minBoundary = InputBoundaries.min
        maxBoundary = InputBoundaries.max
    },
        []
    )

    const nextGuessHandler = (direction) => {
        if ((direction === 'lower' && currentGuess < enteredNumber)
            || (direction === 'higher' && currentGuess > enteredNumber)) {
            Alert.alert('არ მოიტყუო', 'მოტყუება ცუდი საქციელია', [{ text: 'ბოდიში', style: 'cancel' }])
            return;
        }
        if (direction === 'lower') {
            maxBoundary = currentGuess;
        } else if (direction === 'higher') {
            minBoundary = currentGuess + 1
        };

        const nextGuess = generateRandomBetween(minBoundary, maxBoundary, currentGuess)
        setCurrentGuess(_ => nextGuess)
        setGuessRounds(prevState => [nextGuess, ...prevState])
    }

    const numberOfGuesses =guessRounds.length
    return (
        <View style={styles.screen}>
            <Title>ვარაუდი</Title>
            <NumberContainer>{currentGuess}</NumberContainer>
            <Card>
                <InstructionText style={styles.instructionText}>მაღალი თუ დაბალი?</InstructionText>
                <View style={styles.buttonsContainer}>
                    <View style={styles.buttonContainer}>
                        <PrimaryButton onPress={nextGuessHandler.bind(this, 'higher')}>
                            <Ionicons name='add' size={24} color='white' />
                        </PrimaryButton>
                    </View>
                    <View style={styles.buttonContainer}>
                        <PrimaryButton onPress={nextGuessHandler.bind(this, 'lower')}>
                            <Ionicons name='remove' size={24} color='white' />
                        </PrimaryButton>
                    </View>
                </View>
            </Card>
            <View style={styles.listContainer}>
                <View>
                    <FlatList
                        data={guessRounds}
                        renderItem={itemData =>
                            <GuessLogItem
                                roundNumber={numberOfGuesses - itemData.index}
                                guess={itemData.item} />}
                        keyExtractor={item => item}
                    />
                </View>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    screen: {
        flex: 1,
        paddingHorizontal: 10,
        paddingVertical: 70,
    },
    instructionText: {
        marginBottom: 12
    },
    buttonsContainer: {
        flexDirection: 'row'
    },
    buttonContainer: {
        flex: 1
    },
    listContainer: {
        flex: 1,
        padding: 16
    }
})

export default GameScreen