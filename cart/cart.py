from flask import Blueprint, request, redirect, url_for, session, render_template, jsonify
from .cart_session import Cart
from app.services import get_object_or_404
from model import Product, ProductSize
from .forms import CartAddProductForm, CartUpdateProductForm

cart_bp = Blueprint('cart_bp', __name__, template_folder='../templates', static_folder='../static', static_url_path='')

'''@cart_bp.route('cart-add/<slug>/', methods=['POST'])
def cart_add(*args, **kwargs):

    cart = Cart(request.cookies.get('sessionid'))
    product = get_object_or_404(Product, Product.slug == kwargs['slug'])
    form = CartAddProductForm()
    if form.validate_on_submit():
        cart.add(product=product, qty=1, size=form.id_size.data, update_qty=False)
    return redirect(url_for('cart_bp.cart_detail'))
'''


@cart_bp.route('cart_detail/', methods=['GET', 'POST'])
def cart_detail(*args, **kwargs):
    cart = Cart()
    form = CartUpdateProductForm()
    context = {
        'cart': cart,
        'form': form
    }
    return render_template('cart/cart_detail.html', context=context)


@cart_bp.route('cart-qty', methods=['GET'])
def update_qty_cart():
    if request.method == 'GET':
        cart = Cart()
        response = {
            'cart_qty': len(cart)
        }
        return jsonify(response)


@cart_bp.route('price', methods=['GET'])
def cart_price():
    if request.method == 'GET':
        cart = Cart()
        response = {
            'price': cart.get_total_price(),
            'price_discount': cart.get_total_discount_price()
        }
        return jsonify(response)


@cart_bp.route('qty', methods=['GET', 'POST'])
def change_qty():
    if request.method == 'GET':
        product = request.args.get('product')
        size = request.args.get('size')
        if product and size:
            product_size = get_object_or_404(ProductSize, ProductSize.product == product, ProductSize.name == size)
            response = {
                'max_qty': product_size.qty,
                'product': product,
                'size': size
            }
            return jsonify(response)

    if request.method == 'POST':
        product = request.form.get('product')
        max_qty = request.form.get('max_qty')
        qty = request.form.get('qty')
        size = request.form.get('size')
        if qty and max_qty:
            cart = Cart()
            qty = int(qty)
            max_qty = int(max_qty)
            if max_qty >= qty > 0:
                cart.cart[product]['qty'] = qty
                cart.save()
                return jsonify({'message': 'Изменения внесены'})
            else:
                jsonify({'message': 'Текущее ко-во больше доступного или не может быть 0'})
        else:
            jsonify({'message': 'Ко-во товара или максимальное ко-во незадано!'})


@cart_bp.route('remove', methods=['POST'])
def remove_cart():
    if request.method == 'POST':
        product = request.form.get('product_id')
        remove_all = request.form.get('remove_all')
        cart = Cart()
        if remove_all:
            cart.clear()
            return jsonify({'Корзина удалена'})
        else:
            cart.remove(product)
            return jsonify({'id': product.split('-')[0]})
