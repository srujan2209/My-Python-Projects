# Basics Websit Script on Connecting through local host using flask Class

from flask import Flask

app=Flask(__name__)

@app.route('/')

def home():
    return "Homepage here!"

@app.route('/about/')
def about():
    return "About Content goes here!"

if __name__=="__main__":
    app.run(debug=True)