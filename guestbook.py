from flask import Flask,render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///D:\\study\\Python\\PythonPrograms\\contact.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class Comments(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    comment=db.Column(db.String(1000))


@app.route('/')
def index():
    result=Comments.query.all()
    return render_template('index.html',result=result)

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
    name=request.form['name']
    comment=request.form['comment']
    # return 'Name is ' +name+ 'and comment is ' +comment

    signature = Comments(name=name,comment=comment)
    db.session.add(signature)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/home')
def home():
    links=['https://www.youtube.com', 'https://bing.com']
    return render_template('example.html',links=links)

if __name__ == '__main__':
    app.run(debug=True)


