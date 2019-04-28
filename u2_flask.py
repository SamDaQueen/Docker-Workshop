from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def base():
	if request.method == "GET":
		return render_template('u2_ui.html')
	elif request.method == "POST":
		uname = request.form['uname']
		pswd = request.form['pswd']
		conn = sqlite3.connect('cred.db')
		print("Database Opened")
		conn.execute('CREATE TABLE IF NOT EXISTS LOGIN (ID INTEGER IDENTITY(1,1) PRIMARY KEY, NAME VARCHAR NOT NULL,PSWD VARCHAR NOT NULL);')
		print("Table Opened")
		cursor = conn.execute("SELECT * FROM LOGIN")
		for row in cursor:
			print(row)
			if uname==row[1]:
				if pswd == row[2]:
					return render_template('success.html')
				else:
					return render_template('failure.html')
			else:
				return render_template('failure.html')
		conn.close()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.3')