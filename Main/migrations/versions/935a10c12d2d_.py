"""empty message

Revision ID: 935a10c12d2d
Revises: 
Create Date: 2021-05-25 11:25:10.806027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '935a10c12d2d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('image', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'user_id', 'product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_user')
    op.drop_table('product')
    # ### end Alembic commands ###