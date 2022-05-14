from flask import Blueprint, render_template, request
from model import Category, Subcategory, Subcategory_type, Product


shop_bp = Blueprint('shop_bp', __name__, template_folder='../templates', static_folder='../static', static_url_path='')



@shop_bp.route('/category/<category>/', methods=['GET'])
def product_list_by_category(*args, **kwargs):
    if request.method == 'GET':
        products = Product.query.filter(Product.category_slug==kwargs['category'], Product.available==True).all()
        category = Category.query.filter(Category.slug==kwargs['category']).first()
        print(products)
        context = {
            'products': products,
            'category': category
        }
        return render_template('shop/product_list.html', context=context)

@shop_bp.context_processor
def navbar_menu():
    categories = Category.query.all()
    
    return {'categories': categories}