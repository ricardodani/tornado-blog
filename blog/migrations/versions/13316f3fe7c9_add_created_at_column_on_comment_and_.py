"""Add created_at column on Comment and User.

Revision ID: 13316f3fe7c9
Revises: 3aaf86411a3c
Create Date: 2014-04-07 17:17:30.064074

"""

# revision identifiers, used by Alembic.
revision = '13316f3fe7c9'
down_revision = '3aaf86411a3c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'comments', sa.Column('created_at', sa.DateTime(), nullable=True,
                              server_default=sa.func.now()))
    op.add_column(
        'users', sa.Column('created_at', sa.DateTime(), nullable=True,
                           server_default=sa.func.now()))


def downgrade():
    op.drop_column('users', 'created_at')
    op.drop_column('comments', 'created_at')
