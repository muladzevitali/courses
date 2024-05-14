import ExpensesOutput from '../components/ExpensesOutput'
import { ExpensesContext } from '../../store/expenses-context'
import { useContext } from 'react'


const AllExpenses = () => {
    const expensesCtx = useContext(ExpensesContext)
    const expenses = expensesCtx.expenses

    return (
        <ExpensesOutput
            expenses={expenses}
            expensesPeriod="Total"
            fallbackText='No registered expenses found'
        />
    )
}

export default AllExpenses