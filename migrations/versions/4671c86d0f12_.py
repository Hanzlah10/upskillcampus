"""empty message

Revision ID: 4671c86d0f12
Revises: 
Create Date: 2021-12-26 12:54:20.935567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4671c86d0f12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('short_urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_url', sa.String(length=500), nullable=False),
    sa.Column('short_id', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('short_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('short_urls')
    # ### end Alembic commands ###
