import { View, StyleSheet, TextInput } from 'react-native'
import { useContext, useLayoutEffect } from 'react'
import IconButton from '../components/ui/IconButton'
import { GlobalStyles } from '../constants/styles'
import { ExpensesContext } from '../../store/expenses-context'
import ExpenseForm from '../components/ManageExpense/ExpenseForm'


const ManageExpense = ({ navigation, route }) => {
    const expenseId = route.params?.expenseId
    const isEditing = !!expenseId
    const screenTitle = isEditing ? 'Edit expense' : 'Add expense'


    const expensesCtx = useContext(ExpensesContext)
    const selectedExpense = expensesCtx.expenses.find(expense => expense.id == expenseId)

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

    const confirmExpenseHandler = (expenseData) => {
        if (isEditing) {
            expensesCtx.updateExpense(expenseId, expenseData)
        } else {
            expensesCtx.addExpense(expenseData)
        }
        navigation.goBack()
    }

    return (
        <View style={styles.container}>
            <ExpenseForm
                onCancel={cancelExpenseChangeHandler}
                onSubmit={confirmExpenseHandler}
                submitButtonLabel={isEditing ? 'Update' : 'Add'}
                isEditing={isEditing}
                defaultValues={selectedExpense}
            />
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
    deleteButtonContainer: {
        marginTop: 16,
        paddingTop: 8,
        borderTopWidth: 2,
        borderTopColor: GlobalStyles.colors.primary200,
        alignItems: 'center'
    }
})

export default ManageExpense