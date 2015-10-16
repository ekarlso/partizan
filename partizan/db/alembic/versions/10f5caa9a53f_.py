"""empty message

Revision ID: 10f5caa9a53f
Revises: None
Create Date: 2015-10-16 15:30:49.548098

"""

# revision identifiers, used by Alembic.
revision = '10f5caa9a53f'
down_revision = None

from alembic import op
import sqlalchemy as sa

from partizan.db import types

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', types.UUID(), nullable=False),
    sa.Column('name', sa.Unicode(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('packages',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', types.UUID(), nullable=False),
    sa.Column('name', sa.Unicode(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parts',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', types.UUID(), nullable=False),
    sa.Column('name', sa.Unicode(length=100), nullable=False),
    sa.Column('package_id', types.UUID(), nullable=True),
    sa.Column('category_id', types.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['package_id'], ['packages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parts')
    op.drop_table('packages')
    op.drop_table('categories')
    ### end Alembic commands ###
