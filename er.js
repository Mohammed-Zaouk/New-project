const fs = require('fs');

class ToDoList {
    constructor() {
        this._storage = [];
    }

    addTask(enter) {
        const task = {
            text: enter,
            completed: false
        };
        this._storage.push(task);
        this.saveTasks();
    }

    completeTask(element) {
        const index = this._storage.findIndex(task => task.text === element);

        if (index !== -1) {
            this._storage[index].completed = !this._storage[index].completed;
            this.saveTasks();
        } else {
            console.log("Task not found in the list");
        }
    }

    display() {
        if (this._storage.length === 0) {
            console.log('No tasks available.');
        } else {
            return this._storage;
        }
    }

    deleteTask(element) {
        const indexToRemove = this._storage.findIndex(task => task.text === element);

        if (indexToRemove === -1) {
            console.log("Task not found in the list");
        } else {
            this._storage.splice(indexToRemove, 1);
            console.log("Task removed successfully");
            this.saveTasks();
        }
    }

    saveTasks() {
        fs.writeFileSync('tasks.json', JSON.stringify(this._storage, null, 2));
    }
}

// Example usage:
const myToDoList = new ToDoList();

myToDoList.addTask('Task 1');
myToDoList.addTask('Task 2');
myToDoList.addTask('Task 1'); // This should trigger the "already inside the list" message
console.log("Tasks:", myToDoList.display());

myToDoList.deleteTask('Task 2');
myToDoList.deleteTask('Task 3'); // This should trigger the "not inside the list" message
console.log("Tasks after deletion:", myToDoList.display());
