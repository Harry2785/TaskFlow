
const API_URL = "http://127.0.0.1:8000";

const taskForm = document.querySelector("#taskForm");
const taskInput = document.querySelector("#taskInput");
const taskList = document.querySelector("#taskList");
const taskCount = document.querySelector("#taskCount");
const message = document.querySelector("#message");
const addButton = document.querySelector("#addButton");

function showMessage(text) {
    message.textContent = text;
}

async function loadTasks() {
    try {
        const response = await fetch(`${API_URL}/tasks`);

        if (!response.ok) {
            throw new Error("Could not load tasks.");
        }

        const tasks = await response.json();
        renderTasks(tasks);
    } catch (error) {
        showMessage("Cannot connect to TaskFlow. Is the backend running?");
    }
}

function renderTasks(tasks) {
    taskList.replaceChildren();

    const completedCount = tasks.filter(task => task.completed).length;
    taskCount.textContent =
        `${completedCount}/${tasks.length} completed`;

    if (tasks.length === 0) {
        const emptyItem = document.createElement("li");
        emptyItem.className = "empty-state";
        emptyItem.textContent = "No tasks yet. Add your first task above!";
        taskList.appendChild(emptyItem);
        return;
    }

    for (const task of tasks) {
        const item = document.createElement("li");
        item.className = "task-item";

        const name = document.createElement("span");
        name.className = "task-name";
        name.textContent = task.name;

        if (task.completed) {
            name.classList.add("completed");
        }

        item.appendChild(name);

        if (!task.completed) {
            const completeButton = document.createElement("button");
            completeButton.className = "complete-button";
            completeButton.textContent = "Complete";

            completeButton.addEventListener("click", async () => {
                await updateTask(task.id);
            });

            item.appendChild(completeButton);
        }

        const deleteButton = document.createElement("button");
        deleteButton.className = "delete-button";
        deleteButton.textContent = "Delete";

        deleteButton.addEventListener("click", async () => {
            await removeTask(task.id);
        });

        item.appendChild(deleteButton);
        taskList.appendChild(item);
    }
}

taskForm.addEventListener("submit", async event => {
    event.preventDefault();

    const name = taskInput.value.trim();

    if (!name) {
        showMessage("Please enter a task name.");
        return;
    }

    addButton.disabled = true;
    showMessage("Adding task...");

    try {
        const response = await fetch(`${API_URL}/tasks`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name: name })
        });

        if (!response.ok) {
            throw new Error("Could not add task.");
        }

        taskInput.value = "";
        showMessage("Task added!");
        await loadTasks();
    } catch (error) {
        showMessage("Could not add task. Check the backend.");
    } finally {
        addButton.disabled = false;
    }
});

async function updateTask(taskId) {
    try {
        const response = await fetch(`${API_URL}/tasks/${taskId}`, {
            method: "PATCH"
        });

        if (!response.ok) {
            throw new Error("Could not complete task.");
        }

        showMessage("Task completed!");
        await loadTasks();
    } catch (error) {
        showMessage("Could not complete task.");
    }
}

async function removeTask(taskId) {
    try {
        const response = await fetch(`${API_URL}/tasks/${taskId}`, {
            method: "DELETE"
        });

        if (!response.ok) {
            throw new Error("Could not delete task.");
        }

        showMessage("Task deleted.");
        await loadTasks();
    } catch (error) {
        showMessage("Could not delete task.");
    }
}

loadTasks();    