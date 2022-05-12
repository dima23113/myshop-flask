"""empty message

Revision ID: 927930db19cd
Revises: fea70281f2f1
Create Date: 2022-05-13 00:19:03.154100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '927930db19cd'
down_revision = 'fea70281f2f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('subcategory_id', sa.Integer(), nullable=True),
    sa.Column('subcategory_type_id', sa.Integer(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('slug', sa.String(length=256), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('specifications', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(decimal_return_scale=2), nullable=True),
    sa.Column('available', sa.Boolean(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('article', sa.String(length=256), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('price_discount', sa.Float(decimal_return_scale=2), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['brand.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['subcategory_id'], ['subcategory.id'], ),
    sa.ForeignKeyConstraint(['subcategory_type_id'], ['subcategory_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
