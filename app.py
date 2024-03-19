from flask import Flask, render_template, send_from_directory, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired, Email
from forms import ContactForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = '12345678'
db = SQLAlchemy(app)


@app.route('/')
def hello_main():
	return 'Hello World!'

@app.route('/shop/')
def hello_shop():
	return 'Hi'


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
	form = ContactForm()

	if form.validate_on_submit():
		# process the form data here
		# for example, send an email
		flash('Your message has been sent!')
		return 'Success!'
	return render_template('contact.html', form=form)

@app.route('/template/')
def hello_template():
	return render_template('index.html', message='Hello World!')

@app.route('/static/<path:filename>')
def send_file(filename):
	return send_from_directory('static', filename)


if __name__ == '__main__':
	app.run(debug=True)