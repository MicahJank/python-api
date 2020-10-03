from flask import *
app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == "Micah" and password == "google":
        return f"Welcome {username}" 

if __name__ == "__main__":
    app.run(debug=True)