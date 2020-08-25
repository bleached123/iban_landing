from flask import Flask, render_template, request
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET_KEY"
#app.config = config

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'email@email.com'
app.config["MAIL_PASSWORD"] = 'your-password'

mail = Mail(app)


@app.route('/' , methods=['GET', 'POST'])
def home():
	return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact_mail():
	form = request.form
	name = form['name']
	email = form['email']
	subject = form['subject']
	message = form['message']
	return "Thanks for getting in touch, well get back to your shortly"



if __name__ == "__main__":
	app.run()
