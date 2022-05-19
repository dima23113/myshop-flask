from flask import Blueprint, request, redirect, url_for
from .cart_session import Cart
from app.services import get_object_or_404
from model import Product
from .forms import CartAddProductForm
cart_bp = Blueprint('cart_bp', __name__, template_folder='../templates', static_folder='../static', static_url_path='')


@cart_bp.route('cart-add/<slug>/', methods=['POST'])
def cart_add(*args, **kwargs):
    print(request)
    cart = Cart(request)
    product = get_object_or_404(Product, Product.slug == kwargs['slug'])
    form = CartAddProductForm()
    if form.validate_on_submit():
        cart.add(product=product, qty=1, size=form.size.data, update_qty=False)
    return redirect(url_for('cart_bp.cart_detail'))


