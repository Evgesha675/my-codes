const tasksContainer = document.getElementById('tasks');
const taskModal = document.getElementById('task-modal');

function createTask() {
    taskModal.classList.remove('hidden');
}

function saveTask() {
    const taskTitle = document.getElementById('taskTitle').value;
    const taskDescription = document.getElementById('taskDescription').value;

    if (taskTitle.trim() !== '') {
        const taskElement = document.createElement('li');
        taskElement.classList.add('task');
        taskElement.innerHTML = `<strong>${taskTitle}</strong><p>${taskDescription}</p>`;
        taskElement.onclick = () => editTask(taskElement);

        tasksContainer.appendChild(taskElement);
        closeTaskModal();
    }
}

function editTask(taskElement) {
    const title = taskElement.querySelector('strong').textContent;
    const description = taskElement.querySelector('p').textContent;

    document.getElementById('taskTitle').value = title;
    document.getElementById('taskDescription').value = description;

    taskModal.classList.remove('hidden');
    taskElement.remove();
}

function closeTaskModal() {
    document.getElementById('taskTitle').value = '';
    document.getElementById('taskDescription').value = '';
    taskModal.classList.add('hidden');
}

// Закрываем модальное окно при клике вне его области
window.onclick = function (event) {
    if (event.target === taskModal) {
        closeTaskModal();
    }
};
