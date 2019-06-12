from flask import Flask, request, render_template, url_for
app = Flask(__name__)

@app.route('/')
def loginPage(invalid = None):
    return render_template('login/login.html')

@app.route('/loginConfirm')
def login():
    return 'WIP'

@app.route('/register')
def registerPage():
    return 'WIP'

if __name__ == '__main__':
    app.run()
