import { useState } from 'react'

import { View, TextInput, StyleSheet, Alert, useWindowDimensions, KeyboardAvoidingView, ScrollView } from 'react-native'
import PrimaryButton from '../components/ui/PrimaryButton'
import Colors from '../constants/colors'
import InputBoundaries from '../constants/inputBoundaries'
import Title from '../components/ui/Title'
import Card from '../components/ui/Card'
import InstructionText from '../components/ui/InstructionText'

const StartGameScreen = ({ onEnterNumber }) => {
    const [enteredNumber, setEnteredNumber] = useState('')

    const { height } = useWindowDimensions();

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

    const marginTopDistance = height < 380 ? 30 : 100;
    return (
        <ScrollView style={styles.screen}>
            <KeyboardAvoidingView style={styles.screen} behavior='position'>
                <View style={[styles.rootContainer, { marginTop: marginTopDistance }]}>
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
            </KeyboardAvoidingView>
        </ScrollView>
    )
}


//const deviceHight = Dimensions.get('window').height

const styles = StyleSheet.create({
    screen: {
        flex: 1
    },
    rootContainer: {
        flex: 1,
        //marginTop: deviceHight < 380 ? 30 : 100,
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