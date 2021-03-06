"""empty message

Revision ID: eb7a82ba8a2b
Revises: 1f9ee66a852e
Create Date: 2019-05-29 21:08:21.126381

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'eb7a82ba8a2b'
down_revision = '1f9ee66a852e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('email', table_name='user')
    op.drop_column('user', 'email')
    op.drop_column('user', 'username')
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('user', sa.Column('username', mysql.VARCHAR(length=64), nullable=True))
    op.add_column('user', sa.Column('email', mysql.VARCHAR(length=64), nullable=True))
    op.create_index('email', 'user', ['email'], unique=True)
    # ### end Alembic commands ###
