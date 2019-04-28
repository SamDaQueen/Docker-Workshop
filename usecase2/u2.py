from tkinter import *
import sqlite3

def newWindow():
	new = Toplevel(root)
	label_new = Label(new, text="Enter new credentials:").pack()
	label_new_name = Label(new, text="Enter username:").pack()
	entry_new_name = Entry(new)
	entry_new_name.pack()
	label_new_password = Label(new, text="Enter password:").pack()
	entry_new_password = Entry(new)
	entry_new_password.pack()
	res_new = StringVar()
	submit_new = Button(new, text="Save", command=lambda: saveNew(entry_new_name.get(), entry_new_password.get())).pack()
	text_res_new = Label(new, textvariable=res_new, justify=LEFT).pack()
	new.mainloop()

def saveNew(uname, pswd):
	conn = sqlite3.connect('cred.db')
	print("Database Opened")
	conn.execute('CREATE TABLE IF NOT EXISTS LOGIN (ID INTEGER IDENTITY(1,1) PRIMARY KEY, NAME VARCHAR NOT NULL,PSWD VARCHAR NOT NULL);')
	print("Table Opened")
	res.set("Results")
	conn.execute("INSERT INTO LOGIN(NAME, PSWD) VALUES ('" + uname + "','" + pswd + "');")
	conn.commit()
	print("Credentials added")
	conn.close()
	    
def checkLogin():
	uname = entry_name.get()
	pswd = entry_password.get()
	conn = sqlite3.connect('cred.db')
	print("Database Opened")
	conn.execute('CREATE TABLE IF NOT EXISTS LOGIN (ID INTEGER IDENTITY(1,1) PRIMARY KEY, NAME VARCHAR NOT NULL,PSWD VARCHAR NOT NULL);')
	print("Table Opened")
	cursor = conn.execute("SELECT * FROM LOGIN")
	res.set("Results")
	for row in cursor:
		print(row)
		if uname==row[1]:
			if pswd == row[2]:
				res.set("Login Successful")
				newWindow()
				break
			else:
				res.set("Login failed")
				print("Fetched emails")
		else:
			res.set("Login failed")
	conn.close()
	
root = Tk()
root.title("U2")
label_name = Label(root, text="Enter username:").pack()
entry_name = Entry(root)
entry_name.pack()
label_password = Label(root, text="Enter password:").pack()
entry_password = Entry(root)
entry_password.pack()
res = StringVar()
submit = Button(root, text="Login", command=checkLogin).pack()
text_res = Label(root, textvariable=res, justify=LEFT).pack()

root.mainloop()

