from flask import *
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == "Micah" and password == "google":
        return f"Welcome {username}"

if __name__ == "__main__":
    app.run(debug=True)