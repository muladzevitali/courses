import ExpensesOutput from '../components/ExpensesOutput'
import { useContext, useEffect, useState } from 'react'
import { ExpensesContext } from '../../store/expenses-context'
import { getDateMinusDays } from '../utils/date'
import { fetchExpenses } from '../utils/http'
import LoadingOverlay from '../components/ui/LoadingOverlay'
import ErrorOverlay from '../components/ui/ErrorOverlay'


const RecentExpenses = () => {
    const [isFetching, setIsFetching] = useState(true)
    const [error, setError] = useState()
    const expensesCtx = useContext(ExpensesContext)

    useEffect(() => {
        const getExpenses = async () => {
            try {
                const expenses = await fetchExpenses()
                expensesCtx.setExpenses(expenses)
            } catch (error) {
                setError("Couldn't fetch expenses")
            }

            setIsFetching(_ => false)
        }
        getExpenses()

    }, [error])

    const recentExpenses = expensesCtx.expenses.filter(expense => {
        const today = new Date()
        const date7DaysAgo = getDateMinusDays(today, 7)
        return expense.date >= date7DaysAgo
    })

    const errorHandler = () => {
        setError(_ => null)
    }

    if (error && !isFetching) {
        return <ErrorOverlay message={error} onConfirm={errorHandler} />
    }

    if (isFetching) {
        return <LoadingOverlay />
    }

    return (
        <ExpensesOutput
            expenses={recentExpenses}
            expensesPeriod='Last 7 days'
            fallbackText='No expenses registered for last 7 days'
        />
    )
}


export default RecentExpenses