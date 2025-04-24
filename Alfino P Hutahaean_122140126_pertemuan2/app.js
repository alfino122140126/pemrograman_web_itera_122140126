class Dashboard {
  constructor() {
    this.schedule = JSON.parse(localStorage.getItem("schedule")) || [];
    this.tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    this.notes = JSON.parse(localStorage.getItem("notes")) || [];
  }

  saveData() {
    localStorage.setItem("schedule", JSON.stringify(this.schedule));
    localStorage.setItem("tasks", JSON.stringify(this.tasks));
    localStorage.setItem("notes", JSON.stringify(this.notes));
  }

  addSchedule = (schedule) => {
    if (schedule && schedule.trim() !== "") {
      this.schedule.push(schedule);
      this.saveData();
      this.renderSchedule();
    } else {
      alert("Masukkan jadwal kuliah terlebih dahulu.");
    }
  };

  addTask = (task) => {
    if (task && task.trim() !== "") {
      this.tasks.push(task);
      this.saveData();
      this.renderTasks();
    } else {
      alert("Masukkan tugas terlebih dahulu.");
    }
  };

  addNote = (note) => {
    if (note && note.trim() !== "") {
      this.notes.push(note);
      this.saveData();
      this.renderNotes();
    } else {
      alert("Masukkan catatan terlebih dahulu.");
    }
  };

  deleteItem = (array, index) => {
    array.splice(index, 1);
    this.saveData();
    this.renderAll();
  };

  editItem = (array, index) => {
    const newItem = prompt("Edit item:", array[index]);
    if (newItem !== null && newItem !== "") {
      array[index] = newItem;
      this.saveData();
      this.renderAll();
    }
  };

  renderSchedule = () => {
    const scheduleList = document.getElementById("schedule-list");
    scheduleList.innerHTML = "";
    this.schedule.forEach((schedule, index) => {
      const li = document.createElement("li");
      li.innerHTML = `
                <span>${schedule}</span>
                <div class="actions">
                    <button class="edit-btn" onclick="dashboard.editItem(dashboard.schedule, ${index})">✏️</button>
                    <button class="delete-btn" onclick="dashboard.deleteItem(dashboard.schedule, ${index})">X</button>
                </div>
            `;
      scheduleList.appendChild(li);
    });
  };

  renderTasks = () => {
    const tasksList = document.getElementById("tasks-list");
    tasksList.innerHTML = "";
    this.tasks.forEach((task, index) => {
      const li = document.createElement("li");
      li.innerHTML = `
                <span>${task}</span>
                <div class="actions">
                    <button class="edit-btn" onclick="dashboard.editItem(dashboard.tasks, ${index})">✏️</button>
                    <button class="delete-btn" onclick="dashboard.deleteItem(dashboard.tasks, ${index})">X</button>
                </div>
            `;
      tasksList.appendChild(li);
    });
  };

  renderNotes = () => {
    const notesList = document.getElementById("notes-list");
    notesList.innerHTML = "";
    this.notes.forEach((note, index) => {
      const li = document.createElement("li");
      li.innerHTML = `
                <span>${note}</span>
                <div class="actions">
                    <button class="edit-btn" onclick="dashboard.editItem(dashboard.notes, ${index})">✏️</button>
                    <button class="delete-btn" onclick="dashboard.deleteItem(dashboard.notes, ${index})">X</button>
                </div>
            `;
      notesList.appendChild(li);
    });
  };

  renderAll = () => {
    this.renderSchedule();
    this.renderTasks();
    this.renderNotes();
  };
}

const dashboard = new Dashboard();
dashboard.renderAll();

document.getElementById("add-schedule").addEventListener("click", () => {
  const scheduleInput = document.getElementById("schedule-input");
  const schedule = scheduleInput.value;
  if (schedule) {
    dashboard.addSchedule(schedule);
    scheduleInput.value = "";
  } else {
    alert("Jadwal tidak boleh kosong!");
  }
});

document.getElementById("add-task").addEventListener("click", () => {
  const taskInput = document.getElementById("task-input");
  const task = taskInput.value;
  if (task) {
    dashboard.addTask(task);
    taskInput.value = "";
  } else {
    alert("Tugas tidak boleh kosong!");
  }
});

document.getElementById("add-note").addEventListener("click", () => {
  const noteInput = document.getElementById("note-input");
  const note = noteInput.value;
  if (note) {
    dashboard.addNote(note);
    noteInput.value = "";
  } else {
    alert("Catatan tidak boleh kosong!");
  }
});
