from flask import Blueprint, render_template, request, redirect, url_for
from model import Category, Subcategory, Subcategory_type, Product, ImageProduct, ProductSize
from cart.forms import CartAddProductForm
from cart.cart_session import Cart
from app.services import get_object_or_404
import os

shop_bp = Blueprint('shop_bp', __name__, template_folder='../templates', static_folder='../static', static_url_path='')


@shop_bp.route('/', methods=['GET'])
def index(*args, **kwargs):
    print(request.cookies.get('sessionid'))
    return render_template('base.html')


@shop_bp.route('/category/', methods=['GET'])
def product_list(*args, **kwargs):
    products = Product.query.filter(Product.available == True).all()
    context = {
        'products': products
    }
    return render_template('shop/product_list.html', context=context)


@shop_bp.route('/category/<category>/', methods=['GET'])
def product_list_by_category(*args, **kwargs):
    if request.method == 'GET':
        products = Product.query.filter(Product.category_slug == kwargs['category'], Product.available == True).all()
        category = Category.query.filter(Category.slug == kwargs['category']).first()
        context = {
            'products': products,
            'category': category
        }
        return render_template('shop/product_list.html', context=context)


@shop_bp.route('/products/<slug>/', methods=['GET', 'POST'])
def product_detail(*args, **kwargs):
    form = CartAddProductForm()
    print(form.data)
    if form.validate_on_submit():
        print(form.data)
        cart = Cart(request.cookies.get('sessionid'))
        product = get_object_or_404(Product, Product.slug == kwargs['slug'])
        cart.add(product=product, qty=1, size=form.id_size.data, update_qty=False)
        return redirect(url_for('cart_bp.cart_detail'))
    product = Product.query.filter_by(slug=kwargs['slug']).first()
    recommendations = Product.query.all()[:6]
    product_image = ImageProduct.query.filter(ImageProduct.product == product.id).all()
    sizes = ProductSize.query.filter(ProductSize.product == product.id).all()
    context = {
        'product': product,
        'recommendations': recommendations,
        'images': product_image,
        'sizes': sizes
    }
    return render_template('shop/product_detail.html', context=context, form=form)


@shop_bp.app_context_processor
def navbar_menu():
    categories = Category.query.all()

    return {'categories': categories}


@shop_bp.app_template_filter('get_path')
def get_path(p):
    print(os.path.split(p))
    return os.path.split(p)[1]


@shop_bp.app_template_filter('unordered_list')
def unordered_list(specification):
    spec = ['Характеристики:']
    var = specification.split('\n')
    spec.append(var)
    return spec
