import tkinter as tk
from tkinter import messagebox
import json

# Save tasks to a file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(task_list.get(0, tk.END), file)

# Load tasks from a file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                task_list.insert(tk.END, task)
    except FileNotFoundError:
        pass  

# Add a new task
def add_task():
    task = task_entry.get()  
    if task:  
        task_list.insert(tk.END, task) 
        task_entry.delete(0, tk.END)  
        save_tasks() 
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")  


# Remove selected task
def delete_task():
    try:
        selected = task_list.curselection()[0]
        task_list.delete(selected)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

# Mark task as completed
def mark_completed():
    try:
        selected = task_list.curselection()[0]
        task = task_list.get(selected)
        task_list.delete(selected)
        task_list.insert(tk.END, f"✔ {task}")
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as completed!")


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_list = tk.Listbox(root, width=50, height=15)
task_list.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

complete_button = tk.Button(root, text="Mark Completed", command=mark_completed)
complete_button.pack()

load_tasks()  

root.mainloop()
