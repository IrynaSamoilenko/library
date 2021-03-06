"""empty message

Revision ID: f9364a5d92b4
Revises: afe50b8a7822
Create Date: 2019-05-29 22:49:14.500423

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f9364a5d92b4'
down_revision = 'afe50b8a7822'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=False))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', mysql.VARCHAR(length=128), nullable=False))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
