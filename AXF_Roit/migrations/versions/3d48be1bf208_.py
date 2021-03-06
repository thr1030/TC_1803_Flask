"""empty message

Revision ID: 3d48be1bf208
Revises: 
Create Date: 2018-06-12 15:12:08.697669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d48be1bf208'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('axf_mustbuy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('trackid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('axf_nav',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('trackid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('axf_shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('trackid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('axf_wheel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('trackid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('axf_wheel')
    op.drop_table('axf_shop')
    op.drop_table('axf_nav')
    op.drop_table('axf_mustbuy')
    # ### end Alembic commands ###
