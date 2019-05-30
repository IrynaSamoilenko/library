"""empty message

Revision ID: afe50b8a7822
Revises: d516996dee73
Create Date: 2019-05-29 22:21:05.607261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afe50b8a7822'
down_revision = 'd516996dee73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('m2m_authors_ibfk_2', 'm2m_authors', type_='foreignkey')
    op.create_foreign_key(None, 'm2m_authors', 'books', ['book_id'], ['id'])
    op.drop_constraint('m2m_categories_ibfk_1', 'm2m_categories', type_='foreignkey')
    op.create_foreign_key(None, 'm2m_categories', 'books', ['book_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'm2m_categories', type_='foreignkey')
    op.create_foreign_key('m2m_categories_ibfk_1', 'm2m_categories', 'users', ['book_id'], ['id'])
    op.drop_constraint(None, 'm2m_authors', type_='foreignkey')
    op.create_foreign_key('m2m_authors_ibfk_2', 'm2m_authors', 'users', ['book_id'], ['id'])
    # ### end Alembic commands ###