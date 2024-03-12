import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30, fg='blue')
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task,bg='aqua',fg='red')
add_button.pack()

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30,bg='grey',fg='yellow')
listbox.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task,bg='crimson')
remove_button.pack()

root.mainloop()