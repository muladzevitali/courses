import axios from 'axios'


const BACKEND_URL = 'url'


export const storeExpense = async (expenseData) => {
    const response = await axios.post(BACKEND_URL + '/expenses.json', expenseData)

    return response.data.name
}


export const fetchExpenses = async () => {
    const response = await axios.get(BACKEND_URL + '/expenses.json')

    const expenses = []
    for (const key in response.data) {
        const expense = {
            id: key,
            amount: response.data[key].amount,
            date: new Date(response.data[key].date),
            description: response.data[key].description,
        }
        expenses.push(expense)
    }
    return expenses;
}


export const updateExpense = (id, expenseData) => {
    return axios.put(BACKEND_URL + `/expenses/${id}.json`, expenseData)
}


export const deleteExpense = async (id) => {
    axios.delete(BACKEND_URL + `/expenses/${id}.json`)
}
