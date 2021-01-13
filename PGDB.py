from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config.update(
    SECRET_KEY="topsecret",
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:12345@localhost/catalog_db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
db = SQLAlchemy(app)

class Publication(db.Model):
    __tablename__ = "publication"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable = False)

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "Name is {}".format(self.name)

class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_raiting = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    #Relationship

    pub_id = db.Column(db.Integer, db.ForeignKey("publication.id"))

    def __init__(self, title, author, avg_raiting, book_format, image, num_pages, pub_id):
        #self.id = id
        self.title = title
        self.author = author
        self.avg_raiting = avg_raiting
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

db.create_all()

@app.route("/")
def home():
    return "Hello"

#if __name__ == "__main__":

