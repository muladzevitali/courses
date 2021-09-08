import './Expenses.css'
import Card from '../UI/Card'
import ExpensesFilter from "./ExpensesFilter";
import {useState} from "react";
import ExpensesList from './ExpensesList'
import ExpensesChart from "./ExpensesChart";

function Expenses(props) {
    const [filteredYear, setFilteredYear] = useState('2020')
    const [isYearFiltered, setIsYearFiltered] = useState(false);

    const filterChangeHandler = year => {
        setFilteredYear(year);
        setIsYearFiltered(true);
    }

    const filteredExpenses = isYearFiltered ?
        props.expenses.filter(expense => expense.date.getFullYear().toString() === filteredYear) : props.expenses;


    return (
        <Card className='expenses'>
            <ExpensesChart expenses={filteredExpenses}/>
            <ExpensesFilter onChangeFilter={filterChangeHandler} selected={filteredYear}/>
            <ExpensesList expenses={filteredExpenses}/>
        </Card>
    )
}

export default Expenses;