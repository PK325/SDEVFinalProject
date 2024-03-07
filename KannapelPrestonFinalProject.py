import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, master):
        """
        Initializes the application. 
        """
        self.master = master
        self.master.title("To-Do Tracker")
        self.tasks = []  # Holds tasks

        # Frame for task entry and "Add Task" button
        self.entry_frame = tk.Frame(master)
        self.entry_frame.pack(pady=10)
        self.task_var = tk.StringVar()  # Holds task entry text
        self.task_entry = tk.Entry(self.entry_frame, textvariable=self.task_var)
        self.task_entry.pack(side="left", padx=5)

        # Load and resize images
        self.add_image = tk.PhotoImage(file="add.png").subsample(50)
        self.edit_image = tk.PhotoImage(file="edit.png").subsample(50)
        self.delete_image = tk.PhotoImage(file="delete.png").subsample(50)

        # "Add Task" button with image
        self.add_button = tk.Button(self.entry_frame, image=self.add_image, command=self.add_task, bd=0)
        self.add_button.pack(side="left")
        tk.Label(self.entry_frame, text="Add Task").pack(side="left")

        # Frame for the task list
        self.task_frame = tk.Frame(master)
        self.task_frame.pack(pady=10)

        # Display the task list
        self.update_task_listbox()

    def add_task(self):
        """
        Adds a new task.
        """
        task = self.task_var.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def edit_task(self, task):
        """
        Edits an existing task.
        """
        edited_task = simpledialog.askstring("Edit Task", "Enter the new task:", initialvalue=task)
        if edited_task:
            self.tasks[self.tasks.index(task)] = edited_task
            self.update_task_listbox()

    def remove_task(self, task):
        """
        Removes a task.
        """
        self.tasks.remove(task)
        self.update_task_listbox()

    def update_task_listbox(self):
        """
        Updates the task list display.
        """
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            tk.Checkbutton(self.task_frame, text=task).grid(row=i, column=0, sticky=tk.W)
            tk.Button(self.task_frame, image=self.edit_image, command=lambda t=task: self.edit_task(t), bd=0).grid(row=i, column=1)
            tk.Button(self.task_frame, image=self.delete_image, command=lambda t=task: self.remove_task(t), bd=0).grid(row=i, column=2)
            tk.Label(self.task_frame, text="Edit").grid(row=i+1, column=1)
            tk.Label(self.task_frame, text="Delete").grid(row=i+1, column=2)

def main():
    root = tk.Tk()
    root.geometry("400x300")
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
