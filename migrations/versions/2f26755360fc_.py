"""empty message

Revision ID: 2f26755360fc
Revises: 0d71713e19d9
Create Date: 2022-05-14 13:47:12.777930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f26755360fc'
down_revision = '0d71713e19d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'brand', ['slug'])
    op.add_column('product', sa.Column('subcategory_slug', sa.String(length=256), nullable=True))
    op.add_column('product', sa.Column('subcategory_type_slug', sa.String(length=256), nullable=True))
    op.add_column('product', sa.Column('brand_slug', sa.String(length=256), nullable=True))
    op.drop_constraint('product_brand_id_fkey', 'product', type_='foreignkey')
    op.drop_constraint('product_subcategory_type_id_fkey', 'product', type_='foreignkey')
    op.drop_constraint('product_subcategory_id_fkey', 'product', type_='foreignkey')
    op.create_foreign_key(None, 'product', 'subcategory_type', ['subcategory_type_slug'], ['slug'])
    op.create_foreign_key(None, 'product', 'subcategory', ['subcategory_slug'], ['slug'])
    op.create_foreign_key(None, 'product', 'brand', ['brand_slug'], ['slug'])
    op.drop_column('product', 'brand_id')
    op.drop_column('product', 'subcategory_id')
    op.drop_column('product', 'subcategory_type_id')
    op.add_column('subcategory', sa.Column('category_slug', sa.String(length=55), nullable=True))
    op.create_unique_constraint(None, 'subcategory', ['slug'])
    op.drop_constraint('subcategory_category_id_fkey', 'subcategory', type_='foreignkey')
    op.create_foreign_key(None, 'subcategory', 'category', ['category_slug'], ['slug'])
    op.drop_column('subcategory', 'category_id')
    op.add_column('subcategory_type', sa.Column('subcategory_slug', sa.String(length=55), nullable=True))
    op.create_unique_constraint(None, 'subcategory_type', ['slug'])
    op.drop_constraint('subcategory_type_subcategory_id_fkey', 'subcategory_type', type_='foreignkey')
    op.create_foreign_key(None, 'subcategory_type', 'subcategory', ['subcategory_slug'], ['slug'])
    op.drop_column('subcategory_type', 'subcategory_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subcategory_type', sa.Column('subcategory_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'subcategory_type', type_='foreignkey')
    op.create_foreign_key('subcategory_type_subcategory_id_fkey', 'subcategory_type', 'subcategory', ['subcategory_id'], ['id'])
    op.drop_constraint(None, 'subcategory_type', type_='unique')
    op.drop_column('subcategory_type', 'subcategory_slug')
    op.add_column('subcategory', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'subcategory', type_='foreignkey')
    op.create_foreign_key('subcategory_category_id_fkey', 'subcategory', 'category', ['category_id'], ['id'])
    op.drop_constraint(None, 'subcategory', type_='unique')
    op.drop_column('subcategory', 'category_slug')
    op.add_column('product', sa.Column('subcategory_type_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('product', sa.Column('subcategory_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('product', sa.Column('brand_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.create_foreign_key('product_subcategory_id_fkey', 'product', 'subcategory', ['subcategory_id'], ['id'])
    op.create_foreign_key('product_subcategory_type_id_fkey', 'product', 'subcategory_type', ['subcategory_type_id'], ['id'])
    op.create_foreign_key('product_brand_id_fkey', 'product', 'brand', ['brand_id'], ['id'])
    op.drop_column('product', 'brand_slug')
    op.drop_column('product', 'subcategory_type_slug')
    op.drop_column('product', 'subcategory_slug')
    op.drop_constraint(None, 'brand', type_='unique')
    # ### end Alembic commands ###
