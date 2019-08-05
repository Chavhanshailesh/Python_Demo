#pip install flask-sqlalchemy
#from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class students(db.Model):
	id = db.Column('student_id', db.Integer, primary_key= True)
	name = db.Column(db.String(100))
	city = db.Column(db.String(100))
	pin = db.Column(db.String(10))

def __init__(self, name,city,pin):
	self.name = name
	self.city = city
	self.pin = pin

@app.route('/')
def show_all():
	return render_template('show_all.html', students = students.query.all() )


@app.route('/new', methods = ['POST','GET'])
def new():
	if request.method == 'POST':
		if not request.form['name'] or not request.form['city'] or not request.form['pin']:
			flash('please enter all the field','error')
		else:
			student = students(name=request.form['name'],city=request.form['city'],pin=request.form['pin'])

			db.session.add(student)
			db.session.commit()
			flash('record is added')
	return render_template('new.html')



if __name__ == '__main__':
	db.create_all()
	app.run()
