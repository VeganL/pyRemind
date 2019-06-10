from flask import Flask
from functions import *
app = Flask(__name__)

@app.route('/')
def main():
    return landingPage()

if __name__ == '__main__':
    app.run()
