"""Add comments and users table.

Revision ID: 3aaf86411a3c
Revises: 471804f7543
Create Date: 2014-04-07 17:06:45.128236

"""

# revision identifiers, used by Alembic.
revision = '3aaf86411a3c'
down_revision = '471804f7543'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id', 'username')
    )
    op.create_table(
        'comments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('post_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('comments')
    op.drop_table('users')
