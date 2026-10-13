
import { useEffect, useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [tasks, setTasks] = useState([]);
  const [taskName, setTaskName] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  async function loadTasks() {
    try {
      const response = await fetch(`${API_URL}/tasks`);

      if (!response.ok) {
        throw new Error("Could not load tasks.");
      }

      const data = await response.json();
      setTasks(data);
    } catch (error) {
      setMessage("Cannot connect. Is the backend running?");
    }
  }

  useEffect(() => {
  async function fetchTasks() {
    try {
      const response = await fetch(`${API_URL}/tasks`);

      if (!response.ok) {
        throw new Error("Could not load tasks.");
      }

      const data = await response.json();
      setTasks(data);
    } catch (error) {
      setMessage("Cannot connect. Is the backend running?");
    }
  }

  fetchTasks();
}, []);

  async function addTask(event) {
    event.preventDefault();

    const name = taskName.trim();

    if (!name) {
      setMessage("Please enter a task name.");
      return;
    }

    setLoading(true);
    setMessage("");

    try {
      const response = await fetch(`${API_URL}/tasks`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name }),
      });

      if (!response.ok) {
        throw new Error("Could not add task.");
      }

      setTaskName("");
      setMessage("Task added!");
      await loadTasks();
    } catch (error) {
      setMessage("Could not add task.");
    } finally {
      setLoading(false);
    }
  }

  async function completeTask(taskId) {
    try {
      const response = await fetch(`${API_URL}/tasks/${taskId}`, {
        method: "PATCH",
      });

      if (!response.ok) {
        throw new Error("Could not complete task.");
      }

      setMessage("Task completed!");
      await loadTasks();
    } catch (error) {
      setMessage("Could not complete task.");
    }
  }

  async function deleteTask(taskId) {
    try {
      const response = await fetch(`${API_URL}/tasks/${taskId}`, {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error("Could not delete task.");
      }

      setMessage("Task deleted.");
      await loadTasks();
    } catch (error) {
      setMessage("Could not delete task.");
    }
  }

  const completedCount = tasks.filter(
    (task) => task.completed
  ).length;

  return (
    <main className="container">
      <header className="header">
        <p className="eyebrow">YOUR PERSONAL WORKSPACE</p>

        <h1>
          TaskFlow<span>.</span>
        </h1>

        <p className="subtitle">
          One task at a time. Keep moving forward.
        </p>
      </header>

      <section className="panel">
        <form onSubmit={addTask}>
          <label htmlFor="taskInput">
            What do you need to get done?
          </label>

          <div className="input-row">
            <input
              id="taskInput"
              value={taskName}
              onChange={(event) =>
                setTaskName(event.target.value)
              }
              placeholder="e.g. Finish Calculus assignment"
              maxLength={200}
            />

            <button type="submit" disabled={loading}>
              {loading ? "Adding..." : "+ Add task"}
            </button>
          </div>
        </form>

        <p className="message" role="status">
          {message}
        </p>
      </section>

      <section className="panel">
        <div className="section-heading">
          <h2>My tasks</h2>

          <span>
            {completedCount}/{tasks.length} completed
          </span>
        </div>

        {tasks.length === 0 ? (
          <p className="empty-state">
            No tasks yet. Add your first task above!
          </p>
        ) : (
          <ul className="task-list">
            {tasks.map((task) => (
              <li className="task-item" key={task.id}>
                <span
                  className={
                    task.completed
                      ? "task-name completed"
                      : "task-name"
                  }
                >
                  {task.name}
                </span>

                <div className="task-actions">
                  {!task.completed && (
                    <button
                      className="complete-button"
                      onClick={() => completeTask(task.id)}
                    >
                      Complete
                    </button>
                  )}

                  <button
                    className="delete-button"
                    onClick={() => deleteTask(task.id)}
                  >
                    Delete
                  </button>
                </div>
              </li>
            ))}
          </ul>
        )}
      </section>

      <footer>
        Your progress is saved automatically.
      </footer>
    </main>
  );
}

export default App;