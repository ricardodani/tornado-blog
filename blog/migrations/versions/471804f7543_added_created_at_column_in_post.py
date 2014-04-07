"""Added created_at column in post.

Revision ID: 471804f7543
Revises: 3bed46c48b
Create Date: 2014-04-07 16:39:03.810097

"""

# revision identifiers, used by Alembic.
revision = '471804f7543'
down_revision = '3bed46c48b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'posts',
        sa.Column('created_at', sa.DateTime(), nullable=True,
                  server_default=sa.func.now())
    )


def downgrade():
    op.drop_column('posts', 'created_at')
