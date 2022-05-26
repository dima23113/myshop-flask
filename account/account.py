from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, user_unauthorized, current_user
from model import User
from app import login_manager
from app import db
from .forms import *

account_bp = Blueprint('account_bp', __name__, template_folder='../templates', static_folder='../static',
                       static_url_path='')


@login_manager.user_loader
def load_user(user_id):
    print('fi')
    print(User.query.get(user_id))
    return User.query.get(user_id)


@account_bp.route('/', methods=['GET', 'POST'])
@login_required
def account_profile():
    form_bio = ChangeBioForm()
    form_phone = ChangePhoneNumberForm()
    form_password = ChangePasswordForm()
    form_mailing = ChangeMailingForm()
    form_email = ChangeEmailForm()
    form_id = request.args.get('form_id', '')
    if form_bio.validate_on_submit() and form_id == '1':
        current_user.first_name = form_bio.first_name.data
        current_user.second_name = form_bio.last_name.data
        db.session.commit()
        flash('Данные сохранены!')
        return redirect(url_for('account_bp.account_profile'))
    if form_phone.validate_on_submit() and form_id == '2':
        current_user.phone = form_phone.phone.data
        db.session.commit()
        return redirect(url_for('account_bp.account_profile'))
    if form_password.validate_on_submit() and form_id == '3':
        if form_password.password.data == form_password.password2.data:
            current_user.password = generate_password_hash(form_password.password.data)
            db.session.commit()
            return redirect(url_for('account_bp.account_profile'))
    if form_mailing.validate_on_submit() and form_id == '4':
        print(form_mailing.mailing_yes.data)
        current_user.email_mailing = form_mailing.mailing_yes.data
        db.session.commit()
        return redirect(url_for('account_bp.account_profile'))
    if form_email.validate_on_submit() and form_id == '5':
        flash('Обратитесь в ТП сайса для смены почты')
        return redirect(url_for('account_bp.account_profile'))
    context = {
        'form_bio': form_bio,
        'form_phone': form_phone,
        'form_password': form_password,
        'form_mailing': form_mailing,
        'form_email': form_email
    }
    return render_template('account/user_profile.html', context=context)


@account_bp.route('/register', methods=['GET', 'POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    if request.method == 'POST':
        if not (email or password2 or password):
            flash('Заполните поля формы регистрации!')
        elif password != password2:
            flash('Пароли не совпадают')
        else:
            password = generate_password_hash(password)
            new_user = User(email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('account_bp.login'))
    return render_template('account/register.html')


@account_bp.route('/login', methods=['GET', 'POST'])
def login():
    if not user_unauthorized:
        return redirect(url_for('shop_bp.index'))
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        if login and password:
            user = User.query.filter_by(email=email).first()
            print(user)
            if check_password_hash(user.password, password):
                login_user(user)
                next_page = request.args.get('next', url_for('shop_pb.index'))
                return redirect(next_page)
            else:
                flash('Пароль или логин введен неверно!')
        else:
            flash('Заполните поля для входа!')
            return render_template('account/login.html')


@account_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('shop_bp.index'))


@account_bp.after_app_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('account_bp.login') + '?next=' + request.url)
    return response


@account_bp.route('/address', methods=['GET', 'POST'])
@login_required
def change_address():
    form = ChangeAddressForm()
    if form.validate_on_submit():
        current_user.city = form.city.data
        current_user.country = form.country.data
        current_user.zip_code = form.zip_code.data
        current_user.address = form.address.data
        db.session.commit()
        return redirect(url_for('account_bp.change_address'))
    return render_template('account/change_address.html', form=form)


@account_bp.route('/orders', methods=['GET', 'POST'])
@login_required
def orders_list():
    pass


@account_bp.route('/tickets', methods=['GET', 'POST'])
@login_required
def tickets_list():
    pass


@account_bp.route('/favorites', methods=['GET', 'POST'])
@login_required
def favorites_list():
    pass
