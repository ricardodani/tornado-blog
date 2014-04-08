"""Added author column on Post.

Revision ID: 282315e9a00b
Revises: 13316f3fe7c9
Create Date: 2014-04-07 18:00:52.963856

"""

# revision identifiers, used by Alembic.
revision = '282315e9a00b'
down_revision = '13316f3fe7c9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('author_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'author_id')
    ### end Alembic commands ###
