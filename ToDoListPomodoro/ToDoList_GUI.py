import tkinter as tk
import tkinter.messagebox
import pickle


window = tk.Tk()
window.title("To-Do Lista")

def onReturn(*args): #
    task = entry_task.get()
    listbox_tasks.insert(tk.END, task)
    entry_task.delete(0, tk.END)

def add_task(*args):
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        tk.messagebox.showwarning(title="Warning!", message = "You must add task.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tk.messagebox.showwarning(title="Warning!", message = "You must add task.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tk.END)
        for task in tasks:
            listbox_tasks.insert(tk.END, task)
    except:
        tk.messagebox.showwarning(title="Warning!", message = "Can't find tasks.dat file.")



def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    if tasks == ():
        tk.messagebox.showwarning(title="Warning!", message="Don't save empty list of tasks!")
    else:
        pickle.dump(tasks, open("tasks.dat", "wb" ))


def display_msg():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    if tk.messagebox.askyesno('Python Guides', 'Do you want to save changes before you leave?'):
        if tasks == ():
            tk.messagebox.showwarning('Python Guides', 'There is nothing to save ;)')
            pass
        else:
            save_tasks()
            tk.messagebox.showwarning('Python Guides', 'Saved!')
        window.after(0, window.quit)
    else:
        window.after(0, window.quit)

def open_file():
    from PomodoroTimer import PomodoroTimer

#Tworzenie GUI
frame_tasks = tk.Frame(window, bg="#EA4335")
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height = 10, width = 50,bg="#FFEBEB" )
listbox_tasks.pack(side=tk.LEFT) #

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y,)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(window, width=50, bg="#FFEBEB")
entry_task.bind("<Return>", add_task)
entry_task.delete(0, "end")
entry_task.pack()

window.config(background="#EA4335")


button_add_task = tk.Button(window, text = "Add task", width=48, command=add_task,bg="#EA4335")
button_add_task.pack()

button_delete_task = tk.Button(window, text = "Delete task", width=48, command=delete_task, bg="#EA4335")
button_delete_task.pack()

button_load_tasks = tk.Button(window, text = "Load tasks", width=48, command=load_tasks,bg="#EA4335")
button_load_tasks.pack()

button_save_tasks = tk.Button(window, text = "Save tasks", width=48, command=save_tasks,bg="#EA4335")
button_save_tasks.pack()

button_pomodoro = tk.Button(window, text = "Pomodoro", width=48, command=open_file,bg="#EA4335")
button_pomodoro.pack()

window.protocol('WM_DELETE_WINDOW', display_msg)

window.mainloop()