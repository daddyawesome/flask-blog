from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#To where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(100), nullable=False)
     content = db.Column(db.Text, nullable=False )
     author = db.Column(db.String(20), nullable=False, default='N/A')
     date_posted = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)


all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1',
        'author': 'Daddyawesome'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of post 2 post 2post 2post 2post 2post 2'
    }

]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts = all_posts)

@app.route('/home/user/<string:name>/posts/<int:id>')
def hello(name, id):
    return "Hello, " + name +", your id is: " + str(id)

@app.route('/onlyget', methods=['GET'])
def get_req():
    return "You can only get this webpage"

if __name__ == "__main__":
    app.run(debug=True)
