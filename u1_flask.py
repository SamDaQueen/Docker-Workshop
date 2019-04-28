from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def start():
	if request.method == "GET":
		return render_template('u1_ui.html')
	elif request.method == "POST":
		file = open("u1_data.txt", "at")
		file.write(request.form['firstName'] + ' ' + request.form['lastName'] + '<br>')
		file.close()
		file = open("u1_data.txt", "rt")
		res = file.read()
		file.close()
		return res

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.2')