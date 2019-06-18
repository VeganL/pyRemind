from flask import Flask, request, render_template, url_for

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        error = 'Invalid username/password'
    
    return render_template('login.html', error=error)

@app.route('/register')
def registerPage():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()
