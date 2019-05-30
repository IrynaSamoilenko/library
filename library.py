from app import app
from app.models import db, User, Book, Author, \
    Category, Order, m2m_categories, m2m_authors

@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'User': User,
            'Book': Book,
            'Author': Author,
            'Category': Category,
            'Order': Order,
            'm2m_authors': m2m_authors,
            'm2m_categories': m2m_categories}