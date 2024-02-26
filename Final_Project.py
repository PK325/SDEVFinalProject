import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do Tracker")
        self.tasks = []

        # Frame for the task entry and "Add Task" button
        self.entry_frame = tk.Frame(master)
        self.entry_frame.pack(pady=10)

        # Entry field for adding tasks
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.entry_frame, textvariable=self.task_var)
        self.task_entry.pack(side="left", padx=5)

        # Add tasks button
        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side="left")

        # Frame for the task list
        self.task_frame = tk.Frame(master)
        self.task_frame.pack(pady=10)

        # Displays the task list
        self.update_task_listbox()

    def add_task(self):
        # adds a new task
        task = self.task_var.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()  
            self.task_var.set("")  
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def edit_task(self, task):
        # Edits an existing task
        edited_task = simpledialog.askstring("Edit Task", "Enter the new task:", initialvalue=task)
        if edited_task:
            self.tasks[self.tasks.index(task)] = edited_task
            self.update_task_listbox()  

    def remove_task(self, task):
        # Removes a task
        self.tasks.remove(task)
        self.update_task_listbox()  

    def update_task_listbox(self):
        # Updates the task list display
        for widget in self.task_frame.winfo_children():
            widget.destroy() 

        # Recreates the task list
        for i, task in enumerate(self.tasks):
            tk.Checkbutton(self.task_frame, text=task).grid(row=i, column=0, sticky=tk.W)
            tk.Button(self.task_frame, text="Edit", command=lambda t=task: self.edit_task(t)).grid(row=i, column=1)
            tk.Button(self.task_frame, text="Remove", command=lambda t=task: self.remove_task(t)).grid(row=i, column=2)

def main():
    root = tk.Tk()
    root.geometry("400x300")  
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
