import { createContext, useReducer } from "react";


const DUMMY_EXPENSES = [
    { id: 'e1', description: 'A pair of shoes 1', amount: 12.0, date: new Date('2023-12-19') },
    { id: 'e2', description: 'A pair of shoes 2', amount: 13.0, date: new Date('2023-12-20') },
    { id: 'e3', description: 'A pair of shoes 3', amount: 14.0, date: new Date('2023-12-20') },
    { id: 'e4', description: 'A pair of shoes 4', amount: 15.69, date: new Date('2023-12-23') },
    { id: 'e5', description: 'A pair of shoes 5', amount: 16.0, date: new Date('2024-05-13') },
    { id: 'e6', description: 'A pair of shoes 6', amount: 17.59, date: new Date('2024-05-13') },
    { id: 'e7', description: 'A pair of shoes 7', amount: 18.0, date: new Date('2024-05-13') },
    { id: 'e8', description: 'A pair of shoes 8', amount: 19.0, date: new Date('2024-05-13') },
    { id: 'e9', description: 'A pair of shoes 8', amount: 19.0, date: new Date('2024-05-13') },
    { id: 'e10', description: 'A pair of shoes 8', amount: 29.0, date: new Date('2024-05-13') },
    { id: 'e11', description: 'A pair of shoes 8', amount: 39.0, date: new Date('2024-05-13') },
]

export const ExpensesContext = createContext({
    expenses: [],
    addExpense: ({ description, amount, date }) => { },
    deleteExpense: ({ id }) => { },
    updateExpense: ({ id, description, amount, date }) => { }
})

const expensesReducer = (state, action) => {
    switch (action.type) {
        case 'ADD':
            const id = new Date().toString() + Math.random().toString()
            return [{ ...action.payload, id: id }, ...state]
        case 'UPDATE':
            const updatableExpenseIndex = state.findIndex(item => item.id === action.payload.id);
            const updatableExpense = state[updatableExpenseIndex]
            const updatedExpense = { ...updatableExpense, ...action.payload.data }

            const updatedExpenses = [...state]
            updatedExpenses[updatableExpenseIndex] = updatedExpense
            
            return updatedExpenses
        case 'DELETE':
            return state.filter(expense => expense.id !== action.payload)
        default:
            return state
    }
}


const ExpensesContextProvider = ({ children }) => {
    const [expensesState, dispatch] = useReducer(expensesReducer, DUMMY_EXPENSES)

    const addExpense = (expenseData) => {
        dispatch({ type: 'ADD', payload: expenseData })
    }

    const deleteExpense = (id) => {
        dispatch({ type: 'DELETE', payload: id })
    }

    const updateExpense = (id, expenseData) => {
        dispatch({ type: 'UPDATE', payload: { id: id, data: expenseData } })
    }


    const value = {
        expenses: expensesState,
        addExpense: addExpense,
        deleteExpense: deleteExpense,
        updateExpense: updateExpense
    }

    return (
        <ExpensesContext.Provider value={value}>
            {children}
        </ExpensesContext.Provider>
    )
}

export default ExpensesContextProvider