import { View, StyleSheet, Text, Alert } from "react-native"
import Input from "./Input"
import { useState } from "react"
import Button from "../ui/Button"
import { getFormattedDate } from "../../utils/date"
import { GlobalStyles } from "../../constants/styles"


const ExpenseForm = ({ submitButtonLabel, onCancel, onSubmit, defaultValues }) => {

    const [inputValues, setInputValues] = useState({
        amount: {
            value: defaultValues ? defaultValues?.amount.toString() : '',
            isValid: true
        },
        date: {
            value: defaultValues ? getFormattedDate(defaultValues.date) : '',
            isValid: true
        },
        description: {
            value: defaultValues ? defaultValues.description : '',
            isValid: true
        }
    })


    const inputChangeHandler = (inputName, enteredValue) => {
        setInputValues(prevState => ({ ...prevState, [inputName]: { value: enteredValue, isValid: true } }))
    }

    const submitHandler = () => {
        const expenseData = {
            amount: +inputValues.amount.value,
            date: new Date(inputValues.date.value),
            description: inputValues.description.value
        }

        const amountIsValid = !isNaN(expenseData.amount) && expenseData.amount > 0
        const dateIsValid = expenseData.toString() !== 'Invalid Date'
        const descriptionIsValid = expenseData.description.trim().length > 0

        if (!amountIsValid || !dateIsValid || !descriptionIsValid) {
            setInputValues(prevState => {
                return {
                    amount: { value: prevState.amount.value, isValid: amountIsValid },
                    date: { value: prevState.date.value, isValid: dateIsValid },
                    description: { value: prevState.description.value, isValid: descriptionIsValid },
                }
            })
            return
        }
        onSubmit(expenseData)
    }

    const formIsInvalid = !inputValues.amount.isValid || !inputValues.date.isValid || !inputValues.description.isValid
    return (
        <View style={styles.form}>
            <Text style={styles.title}>Your Expense</Text>
            <View style={styles.inputsRow}>
                <Input
                    label='Amount'
                    style={styles.rowInput}
                    invalid={!inputValues.amount.isValid}
                    textInputConfig={{
                        keyboardType: 'decimal-pad',
                        onChangeText: inputChangeHandler.bind(this, 'amount'),
                        value: inputValues.amount.value
                    }}
                />
                <Input
                    label='Date'
                    style={styles.rowInput}
                    invalid={!inputValues.date.isValid}
                    textInputConfig={{
                        placeholder: 'YYYY-MM-DD',
                        maxLength: 10,
                        onChangeText: inputChangeHandler.bind(this, 'date'),
                        value: inputValues.date.value
                    }}
                />
            </View>
            <Input
                label='Description'
                invalid={!inputValues.description.isValid}
                textInputConfig={{
                    multiline: true,
                    autoCorrect: true,
                    autoCapitalize: 'sentences',
                    onChangeText: inputChangeHandler.bind(this, 'description'),
                    value: inputValues.description.value
                }}
            />
            {formIsInvalid && <Text style={styles.errorText}>Invalid input values - please check entered data!</Text>}
            <View style={styles.buttons}>
                <Button mode='flat' onPress={onCancel} style={styles.button}>Cancel</Button>
                <Button onPress={submitHandler} style={styles.button}>{submitButtonLabel}</Button>
            </View>

        </View>
    )
}

const styles = StyleSheet.create({
    form: {
        marginTop: 40
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        color: 'white',
        marginVertical: 24,
        textAlign: 'center'
    },
    inputsRow: {
        flexDirection: 'row',
        justifyContent: 'space-between'
    },
    rowInput: {
        flex: 1
    },
    buttons: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center'
    },
    button: {
        minWidth: 150,
        marginHorizontal: 8
    },
    errorText: {
        textAlign: 'center',
        color: GlobalStyles.colors.error500,
        margin: 8
    }

})


export default ExpenseForm