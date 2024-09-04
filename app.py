from flask import Flask, render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    ToDo = db.Column(db.String(150), nullable=False)
    Desc = db.Column(db.String(1000), nullable=False)
    Date_Created = db.Column(db.DateTime, default=datetime.utcnow)
    

    def __repr__(self) -> str:
        return f"{self.Sno} - {self.ToDo}"

@app.route('/', methods=["GET", "POST"])
def example():
    if request.method == "POST":
        title = request.form.get('title')
        desc = request.form.get('desc')
        print(request.form['title'])
        print(request.form['desc'])
    
        todo = Todo(ToDo=title, Desc=desc)
        db.session.add(todo)
        db.session.commit()
    alltodo = Todo.query.all()
    return render_template('index.html', alltodo=alltodo)



@app.route('/show')
def show():
    alltodo = Todo.query.all()
    print(alltodo)  
    return "heyy"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
