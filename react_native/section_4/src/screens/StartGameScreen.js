import { useState } from 'react'

import { View, TextInput, StyleSheet, Alert, Text } from 'react-native'
import PrimaryButton from '../components/ui/PrimaryButton'
import Colors from '../constants/colors'
import InputBoundaries from '../constants/inputBoundaries'
import Title from '../components/ui/Title'
import Card from '../components/ui/Card'
import InstructionText from '../components/ui/InstructionText'

const StartGameScreen = ({ onEnterNumber }) => {
    const [enteredNumber, setEnteredNumber] = useState('')

    const numberInputHandler = (enteredText) => {
        setEnteredNumber(_ => enteredText)

    }

    const confirmInputHandler = () => {
        const chosenNumber = parseInt(enteredNumber)

        if (isNaN(chosenNumber) || chosenNumber < InputBoundaries.min || chosenNumber > InputBoundaries.max) {
            Alert.alert(
                'არასწორი რიცხვი',
                `რიცხვი უნდა იყოს ${InputBoundaries.min}-დან ${InputBoundaries.max}-მდე`,
                [{ text: 'განახლება', style: 'destructive', onPress: resetInputHandler }]
            )
            return
        }

        onEnterNumber(chosenNumber)
    }

    const resetInputHandler = () => {
        setEnteredNumber(_ => '')
    }
    return (
        <View style={styles.rootContainer}>
            <Title>გამოიცანი რიცხვი</Title>
            <Card>
                <InstructionText>შეიყვანეთ რიცხვი</InstructionText>
                <TextInput
                    style={styles.numberInput}
                    maxLength={4}
                    keyboardType='numeric'
                    autoCapitalize='none'
                    autoCorrect={false}
                    value={enteredNumber}
                    onChangeText={numberInputHandler}
                />
                <View style={styles.buttonsContainer}>
                    <View style={styles.buttonContainer}>
                        <PrimaryButton onPress={resetInputHandler}>განახლება</PrimaryButton>
                    </View>
                    <View style={styles.buttonContainer}>
                        <PrimaryButton onPress={confirmInputHandler}>დადასტურება</PrimaryButton>
                    </View>
                </View>
            </Card>
        </View>
    )
}

const styles = StyleSheet.create({
    rootContainer: {
        flex: 1,
        marginTop: 100,
        alignItems: 'center'
    },
    numberInput: {
        height: 50,
        width: 75,
        fontSize: 32,
        borderBottomColor: Colors.accent500,
        borderBottomWidth: 2,
        color: Colors.accent500,
        marginVertical: 8,
        fontWeight: 'bold',
        textAlign: 'center'
    },
    buttonsContainer: {
        flexDirection: 'row'
    },
    buttonContainer: {
        flex: 1
    }

})

export default StartGameScreen