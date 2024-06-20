import ProjectsSidebar from "./components/ProjectsSidebar.jsx";
import {useState} from "react";
import NoProjectSelected from "./components/NoProjectSelected.jsx";
import NewProject from "./components/NewProject.jsx";
import SelectedProject from "./components/SelectedProject.jsx";

function App() {
    const [projectsState, setProjectsState] = useState({
        selectedProjectId: undefined,
        projects: [],
        tasks: []
    })

    const handleAddTask = (text) => {
        setProjectsState(prevState => {
            const taskId = Math.random()
            const newTask = {text: text, projectId: projectsState.selectedProjectId, id: taskId}
            return {
                ...prevState, tasks: [...prevState.tasks, newTask]
            }
        })
    }

    const handleDeleteTask = (taskId) => {
        setProjectsState(prevState => {
            return {
                ...prevState, tasks: prevState.tasks.filter(task => task.id !== taskId)
            }
        })
    }

    const handleStartAddProject = () => {
        setProjectsState(prevState => ({...prevState, selectedProjectId: null}))
    }

    const handleCancelAddProject = () => {
        setProjectsState(prevState => ({...prevState, selectedProjectId: undefined}))
    }

    const handleAddProject = (projectData) => {
        setProjectsState(prevState => {
            const projectId = Math.random()
            const newProject = {...projectData, id: projectId}
            return {
                ...prevState, selectedProjectId: undefined, projects: [...prevState.projects, newProject]
            }
        })
    }

    const handleSelectProject = (id) => {
        setProjectsState(prevState => ({...prevState, selectedProjectId: id}))
    }

    const handleDeleteProject = (projectId) => {
        setProjectsState(prevState => {
            return {
                ...prevState,
                selectedProjectId: undefined,
                projects: prevState.projects.filter(project.id !== projectId)
            }
        })
    }

    let content;
    if (projectsState.selectedProjectId === undefined) {
        content = <NoProjectSelected onStartAddProject={handleStartAddProject}/>
    } else if (projectsState.selectedProjectId === null) {
        content = <NewProject onAdd={handleAddProject} onCancel={handleCancelAddProject}/>
    } else {
        const selectedProject = projectsState.projects.find(project => project.id === projectsState.selectedProjectId)
        const selectedProjectTasks = projectsState.tasks.filter(task => task.projectId === selectedProject.id)

        content = <SelectedProject project={selectedProject}
                                   tasks={selectedProjectTasks}
                                   onDelete={handleDeleteProject}
                                   onAddTask={handleAddTask}
                                   onDeleteTask={handleDeleteTask}
        />
    }


    return (<main className='h-screen my-8 flex gap-8'>
        <ProjectsSidebar projects={projectsState.projects}
                         selectedProjectId={projectsState.selectedProjectId}
                         onStartAddProject={handleStartAddProject}
                         onSelectProject={handleSelectProject}
        />
        {content}
    </main>);
}

export default App;
