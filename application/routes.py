from flask import Flask, render_template, request, url_for
from application import app

app = Flask(__name__)

# @app.route('/')
# # @app.route('/home')
# def layout():
#     return render_template('layout.html', name='layout')

@app.route('/')
# @app.route('/home')
def home():
    return render_template('home.html', name='Home')




if __name__== "__main__":
    app.run(debug=True)