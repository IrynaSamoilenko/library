from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


m2m_categories = db.Table('m2m_categories',
                        db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True),
                        db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True))

m2m_authors = db.Table('m2m_authors',
                        db.Column('author_id', db.Integer, db.ForeignKey('authors.id'), primary_key=True),
                        db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True))

class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,nullable=False)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    orders = db.relationship('Order', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,nullable=False)
    bookname = db.Column(db.String(128), index=True, nullable=False)
    year = db.Column(db.Integer, index=True)
    bookpath = db.Column(db.String(128), index=True, nullable=False)
    orders = db.relationship('Order', backref='book', lazy='dynamic')
    authors = db.relationship('Author', secondary=m2m_authors, backref=db.backref('books', lazy='dynamic'))
    categories = db.relationship('Category', secondary=m2m_categories,backref=db.backref('books', lazy='dynamic'))

    def __repr__(self):
        return '<Book {}>'.format(self.bookname)


class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(64), index=True, unique=True, nullable=False)

    def __repr__(self):
        return '<Category {}>'.format(self.category)


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(128), index=True, nullable=False)

    def __repr__(self):
        return '<Author {}>'.format(self.category)


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer,db.ForeignKey('books.id'),nullable=False)
    key = db.Column(db.Integer, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    finish = db.Column(db.DateTime, nullable=False)


