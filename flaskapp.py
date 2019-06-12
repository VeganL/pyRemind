from functions import *
app = Flask(__name__)

@app.route('/')
def loginPage():
    return app.send_static_file('./login/login.html')

@app.route('/loginConfirm', methods=['POST'])
def login():
    pass

@app.route('/register')
def registerPage():
    return 'WIP'

if __name__ == '__main__':
    app.run()
