from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def hello_main():
	return 'Hello World!'

@app.route('/shop/')
def hello_shop():
	return 'Hi'

@app.route('/template/')
def hello_template():
	return render_template('index.html', message='Hello World!')

@app.route('/static/<path:filename>')
def send_file(filename):
	return send_from_directory('static', filename)


if __name__ == '__main__':
	app.run(debug=True)