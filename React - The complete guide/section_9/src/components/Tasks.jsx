import NewTask from "./NewTask.jsx";

const Tasks = ({tasks, onAddTask, onDeleteTask}) => {

    return (
        <section>
            <h2 className='text-2xl font-bold text-stone-700 mb-4'>Tasks</h2>
            <NewTask onAddTask={onAddTask}/>
            {tasks.length === 0 && <p className='text-stone-800 mb-4'>This project doesn't have any tasks yet</p>}
            {tasks.length > 0 && (
                <ul className='p-4 mt-8 rounded-md bg-stone-100'>
                    {tasks.map(task =>
                        <li className='flex justify-between my-4 p-4 bg-stone-200' key={task.id}>
                            <span>{task.text}</span>
                            <button className='text-stone-700 hover:text-red-500'
                                    onClick={_ => onDeleteTask(task.id)}
                            >
                                Clear
                            </button>
                        </li>)}
                </ul>
            )}
        < /section>
    )
}

export default Tasks