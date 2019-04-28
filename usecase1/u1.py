from tkinter import *

def saveData():
    file = open("data/u1_data.txt", "at")
    file.write((entry_name.get() or 'no value') + ' ' + entry_password.get() + '\n')
    file.close()
    getData()

def getData():
    file = open("data/u1_data.txt", "rt")
    res.set(file.read())
    file.close()

root = Tk()
root.title("U1")
label_name = Label(root, text="Enter new name:").pack()
entry_name = Entry(root)
entry_name.pack()
label_password = Label(root, text="Enter password:").pack()
entry_password = Entry(root)
entry_password.pack()
submit = Button(root, text="Save", command=saveData).pack()

label_old = Label(root, text="Previously entered pairs: ").pack()
res = StringVar()
text_res = Label(root, textvariable=res, justify=LEFT).pack()
getData()
root.mainloop()
