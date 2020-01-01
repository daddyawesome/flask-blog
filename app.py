from flask import Flask

app = Flask(__name__)

@app.route('/home/user/<string:name>/posts/<int:id>')
def hello(name, id):
    return "Hello, " + name +", your id is: " + str(id)

if __name__ == "__main__":
    app.run(debug=True)
