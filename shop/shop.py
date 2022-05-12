from flask import Blueprint, render_template


shop_bp = Blueprint('shop_bp', __name__, template_folder='templates', static_folder='static', static_url_path='assets')


@shop_bp.route('/')
def category_product_list():
    return 'this is life'