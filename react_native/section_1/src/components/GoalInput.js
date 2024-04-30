import { useState } from 'react'

import { View, TextInput, Button, StyleSheet, Modal, Image } from 'react-native'

const GoalInput = (props) => {
    const [enteredGoalText, setEnteredGoalText] = useState("")

    const goalInputHandler = (enteredText) => {
        setEnteredGoalText(_ => enteredText)
    }

    const addGoalHandler = () => {
        if (!enteredGoalText) {
            return
        }
        props.onAddGoal(enteredGoalText)
        setEnteredGoalText(_ => "")

    }

    return (
        <Modal visible={props.visible} animationType="slide">
            <View style={styles.inputContainer}>
                <Image source={require("../../assets/images/goal.png")} style={styles.image} />
                <TextInput
                    style={styles.textInput}
                    placeholder="Your Goal"
                    onChangeText={goalInputHandler}
                    value={enteredGoalText}
                />
                <View style={styles.buttonContainer}>
                    <View style={styles.button}>
                        <Button
                            title="Add Goal"
                            onPress={addGoalHandler}
                            color="#5e0acc"
                        />
                    </View>
                    <View style={styles.button}>
                        <Button
                            title="Cancel"
                            onPress={props.endCancelGoal}
                            color="#f31282"
                        />
                    </View>
                </View>

            </View>
        </Modal>
    )
}

export default GoalInput;


const styles = StyleSheet.create({
    inputContainer: {
        flex: 1,
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        margingBottom: 24,
        padding: 16,
        backgroundColor: "#311b6b"
    },
    image: {
        width: 100,
        height: 100,
        margin: 20,
    },
    textInput: {
        borderWidth: 1,
        borderRadius: 6,
        borderColor: "#e4d0ff",
        backgroundColor: "#e4d0ff",
        color: "#120438",
        width: "100%",
        height: "20%",
        marginRight: 8,
        padding: 16,

    },
    buttonContainer: {
        flexDirection: "row-reverse",
        marginTop: 16
    },
    button: {
        width: "30%",
        marginHorizontal: 8,
    }
});