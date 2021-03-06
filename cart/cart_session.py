from flask import session
from model import *
from decimal import Decimal
from app.services import get_object_or_404


class Cart(object):
    CART_SESSION_ID = 'cart'

    def __init__(self, new_session=None):
        print(session)
        self.session = session
        cart = self.session.get(self.CART_SESSION_ID)
        if not cart:
            cart = self.session[self.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, qty=1, size=None, update_qty=False):
        print(size)
        product_id = str(product.id) + '-' + size
        if product_id not in self.cart:
            if product.price_discount is None:
                self.cart[product_id] = {
                    'qty': 0,
                    'price': str(product.price),
                    'size': size,
                    'discount_price': str(product.price)
                }
            else:
                self.cart[product_id] = {
                    'qty': 0,
                    'price': str(product.price),
                    'size': size,
                    'discount_price': str(product.price_discount)
                }
        if update_qty:
            self.cart[product_id]['qty'] = qty
        else:
            item_sizes = get_object_or_404(ProductSize, ProductSize.name == size)
            if self.cart[product_id]['qty'] < item_sizes.qty:
                self.cart[product_id]['qty'] += qty
            else:
                pass
        self.save()

    def save(self):
        self.session[self.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        tst2 = []
        for i in product_ids:
            tst2.append(i)
        print(tst2)
        for i in range(len(tst2)):
            t = Product.query.filter(Product.id == tst2[i].split('-')[0])
            self.cart[tst2[i]]['product'] = get_object_or_404(Product, Product.id == tst2[i].split('-')[0])
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    def get_total_discount_price(self):
        return sum(Decimal(item['discount_price']) * item['qty'] for item in self.cart.values())

    def clear(self):
        del self.session[self.CART_SESSION_ID]
        self.session.modified = True
