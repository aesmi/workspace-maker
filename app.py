import tkinter as tk
from tkinter import filedialog, Text
import os

# refer to here: https://www.tutorialspoint.com/python/python_gui_programming.htm
# create our base for our widgets
root = tk.Tk()

# we use a list data structure to keep track of our apps
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        # we read our input from our text file and we split our apps at ','
        tempApps = f.read()
        tempApps = tempApps.split(',')
        print(tempApps)

# WE DEFINE OUR COMMANDS HERE

# we define our add to our list of workspaces command here
def addApp():
    # this iteratively goes through all child widgets of our frame widget
    # we basically clear our labels
    for widget in frame.winfo_children():
        widget.destroy()
    # we create an open file dialog box which starts at our root directory
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executable", ".exe"),("all files", ".")))
    apps.append(filename)
    print(filename)
    # iteratively print labels for our app bar
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        # we basically need to declare pack everytime we create a new widget to append to our root widget
        label.pack()
        
def runApps():
    for app in apps:
        os.startfile(app)
# create our canvas widget which allows us to make shapee
canvas = tk.Canvas(root, height=1028, width=720, bg='#FFFFFF')
# pack tells the geometry manager to organize our widgets in blocks before placing them in the parent widget
canvas.pack()

frame = tk.Frame(root, bg='#FF0000')
# place the frame without our canvas
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# creates open files button
openFile = tk.Button(root, text="Open file", padx=10, pady=5, fg="white", bg="#88FF88", command=addApp)
openFile.pack()

# creates our run app button
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#22FFDD", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# saves our apps into a text file for persisted storage
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')