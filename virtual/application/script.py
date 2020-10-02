from flask import Flask

app = Flask(__name__)

# think of these like routes in node.js, the app routes this file to whatever the browser window is at currently
# right now it is / so whatever page is initially loaded will be used with this file
@app.route('/')

def home():
    return "Hello, this is my first flask website"


# the below example shows how we can pass variable names to the function through the url paramaters
# @app.route('/<name>')

# def home(name):
#     return f"Hello, this is my first flask website...my name is {name}"

if __name__ == "__main__":
    app.run(debug = True)