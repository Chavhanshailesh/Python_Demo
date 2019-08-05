from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')
 	


@app.route('/form', methods=['POST', 'GET'])
def form():
   if request.method == 'POST':
   	   fname = request.form.get('fname')
	   lname = request.form.get('lname')
	   email = request.form.get('email')
	   return '''<h1>First name is:{}</h1><br>
	   			 <h1>First name is:{}</h1><br>
	   			 <h1>First name is:{}</h1><br> '''.format(fname,lname,email)
	   return render_template("register.html")




if __name__ == '__main__':
    app.run(debug=True)