import { View, StyleSheet } from 'react-native'
import { useContext, useLayoutEffect, useState } from 'react'
import IconButton from '../components/ui/IconButton'
import { GlobalStyles } from '../constants/styles'
import { ExpensesContext } from '../../store/expenses-context'
import ExpenseForm from '../components/ManageExpense/ExpenseForm'
import { deleteExpense, storeExpense, updateExpense } from '../utils/http'
import LoadingOverlay from '../components/ui/LoadingOverlay'
import ErrorOverlay from '../components/ui/ErrorOverlay'


const ManageExpense = ({ navigation, route }) => {
    const [isSubmitting, setIsSubmitting] = useState(false)
    const [error, setError] = useState()


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

    const deleteExpenseHandler = async () => {
        setIsSubmitting(true)
        try {
            await deleteExpense(expenseId)
            expensesCtx.deleteExpense(expenseId)
            navigation.goBack()
        } catch (error) {
            setError(_ => "Couldn't delete expense")
            setIsSubmitting(false)
        }
    }

    const cancelExpenseChangeHandler = () => {
        navigation.goBack()
    }

    const confirmExpenseHandler = async (expenseData) => {
        setIsSubmitting(true)

        if (isEditing) {
            try {
                expensesCtx.updateExpense(expenseId, expenseData)
                await updateExpense(expenseId, expenseData)
                navigation.goBack()
            } catch (error) {
                setError(_ => "Couldn't update expense")
                setIsSubmitting(false)
            }

        } else {
            try {
                const id = await storeExpense(expenseData)
                expensesCtx.addExpense({ ...expenseData, id: id })
                navigation.goBack()
            } catch (error) {
                setError(_ => "Couldn't add expense")
                setIsSubmitting(false)
            }
        }
    }

    const errorHandler = () => {
        setError(_ => null)
    }

    if (error && !isSubmitting) {
        return <ErrorOverlay message={error} onSubmit={errorHandler} />
    }
    if (isSubmitting) {
        return <LoadingOverlay />
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