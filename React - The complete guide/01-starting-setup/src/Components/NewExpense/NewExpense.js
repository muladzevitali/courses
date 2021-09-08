import React, {useState} from 'react'
import './NewExpense.css'
import ExpenseForm from './ExpenseForm'

const NewExpense = (props) => {
    const [isAddExpenseFormEnabled, setIsAddExpenseFormEnabled] = useState(false);

    const saveExpenseDataHandler = enteredExpenseData => {
        const expenseData = {
            ...enteredExpenseData,
            id: Math.random()
        };
        props.onAddExpense(expenseData);

    }
    const addNewExpenseButtonHandler = () => setIsAddExpenseFormEnabled(true);
    const disableAddExpenseFormHandler = () => setIsAddExpenseFormEnabled(false);

    let expenseFormContent = <button onClick={addNewExpenseButtonHandler}>Add new expense</button>

    if(isAddExpenseFormEnabled){
        expenseFormContent = <ExpenseForm onSaveExpenseData={saveExpenseDataHandler}
                                          disableHandler={disableAddExpenseFormHandler}/>
    }

    return (
        <div className="new-expense">
            {expenseFormContent}
        </div>
    )
}

export default NewExpense;