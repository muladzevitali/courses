import { View, StyleSheet } from 'react-native'
import { useContext, useLayoutEffect } from 'react'
import IconButton from '../components/ui/IconButton'
import { GlobalStyles } from '../constants/styles'
import Button from '../components/ui/Button'
import { ExpensesContext } from '../../store/expenses-context'


const ManageExpense = ({ navigation, route }) => {
    const expenseId = route.params?.expenseId
    const isEditing = !!expenseId
    const screenTitle = isEditing ? 'Edit expense' : 'Add expense'

    const expensesCtx = useContext(ExpensesContext)

    useLayoutEffect(() => {
        navigation.setOptions({
            title: screenTitle
        })
    }, [navigation, screenTitle])

    const deleteExpenseHandler = () => {
        expensesCtx.deleteExpense(expenseId)
        navigation.goBack()
    }

    const cancelExpenseChangeHandler = () => {
        navigation.goBack()
    }

    const confirmExpenseHandler = () => {
        if (isEditing) {
            expensesCtx.updateExpense(expenseId, {description: 'text!!', amount: 99.99, date: new Date()} )
        } else {
            expensesCtx.addExpense({ description: 'text', amount: 99.99, date: new Date() })
        }
        navigation.goBack()
    }

    return (
        <View style={styles.container}>
            <View style={styles.buttons}>
                <Button mode='flat' onPress={cancelExpenseChangeHandler} style={styles.button}>Cancel</Button>
                <Button onPress={confirmExpenseHandler} style={styles.button}>{isEditing ? 'Update' : 'Add'}</Button>
            </View>
            {isEditing && (
                <View style={styles.deleteButtonContainer}>
                    <IconButton icon='trash' color={GlobalStyles.colors.error500} size={36} onPress={deleteExpenseHandler} />
                </View>
            )
            }

        </View>
    )
}


const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 24,
        backgroundColor: GlobalStyles.colors.primary800
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
    deleteButtonContainer: {
        marginTop: 16,
        paddingTop: 8,
        borderTopWidth: 2,
        borderTopColor: GlobalStyles.colors.primary200,
        alignItems: 'center'
    }
})

export default ManageExpense