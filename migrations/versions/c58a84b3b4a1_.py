"""empty message

Revision ID: c58a84b3b4a1
Revises: 927930db19cd
Create Date: 2022-05-13 10:59:01.876499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c58a84b3b4a1'
down_revision = '927930db19cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.Text(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('mimetype', sa.Text(), nullable=False),
    sa.Column('product', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('img')
    )
    op.create_table('prouduct_size',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('product', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('brand', sa.Column('img', sa.Text(), nullable=True))
    op.add_column('brand', sa.Column('name_img', sa.Text(), nullable=True))
    op.add_column('brand', sa.Column('mimetype', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'brand', ['img'])
    op.add_column('product', sa.Column('img', sa.Text(), nullable=True))
    op.add_column('product', sa.Column('name_img', sa.Text(), nullable=True))
    op.add_column('product', sa.Column('mimetype', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'product', ['img'])
    op.drop_column('product', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('image', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'product', type_='unique')
    op.drop_column('product', 'mimetype')
    op.drop_column('product', 'name_img')
    op.drop_column('product', 'img')
    op.drop_constraint(None, 'brand', type_='unique')
    op.drop_column('brand', 'mimetype')
    op.drop_column('brand', 'name_img')
    op.drop_column('brand', 'img')
    op.drop_table('prouduct_size')
    op.drop_table('image_product')
    # ### end Alembic commands ###
