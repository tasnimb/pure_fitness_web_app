from flask import Flask, render_template, request, url_for
from application.forms import LoginForm
# from application import app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


@app.route('/')
# @app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/book')
def book():
    return render_template('booking.html', title='Book')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/policies')
def policies():
    return render_template('policies.html', title='policies')


@app.route('/login', methods =['GET', 'POST'])
def login():
    error = ""
    form = LoginForm()
    if request.method == "POST" and form.validate():
        email = form.email.data
        password = form.password.data

        if len(email) == 0 or len(password) == 0:
            error = "Please enter your email address and password"
        else:
            return "You are now logged in "
    return render_template("login.html", title="login", form=form, message=error )

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(CustomerLogin)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)




if __name__== "__main__":
    app.run(debug=True)