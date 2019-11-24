from flask import Blueprint, render_template, request, url_for, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, validators, FloatField
from wtforms.validators import DataRequired
from utils import get_data, save_data, upload_image

product = Blueprint('product',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/products/static'
                    )


class AddProductForm(FlaskForm):
    product_name = StringField('Name of product:', validators=[DataRequired()])
    product_description = TextAreaField('Description of product:', validators=[DataRequired()])
    product_price = StringField('Price of product:', validators=[DataRequired()])
    product_image = FileField()
    submit = SubmitField('Add product')


@product.route('/product', methods=['GET', 'POST'])
def get_all_products():
    list_of_products = get_data("blueprints/products/products.json")
    if request.args.getlist('price'):
        filtered_data = []
        for elem in list_of_products:
            if float(elem['price']) == float(str(
                    request.args.getlist('price')[0])):
                filtered_data.append(elem)
        return render_template('all_products.html',
                               title='Products',
                               list_of_products=filtered_data,
                               )
    else:
        return render_template('all_products.html',
                               title='Products',
                               list_of_products=list_of_products,
                               )


@product.route('/product/<id>', methods=['GET'])
def get_product(id):
    list_of_products = get_data("blueprints/products/products.json")
    for product in list_of_products:
        session[id + product['name']] = 'visited'
        if product['id'] == id:
            return render_template(
                'product.html',
                name=product['name'],
                price=product['price'],
                description=product['description'],
                img_name=product['img_name']
            )
    else:
        return render_template(url_for('404.html'))


@product.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = AddProductForm()
    products_list = get_data("blueprints/products/products.json")
    product_id = str(int(products_list[len(products_list) - 1]['id']) + 1) if len(products_list) else "1"
    if request.method == 'POST':
        if form.validate_on_submit():
            data = {
                'id': product_id,
                'name': request.form.get('product_name'),
                'description': request.form.get('product_description'),
                'price': request.form.get('product_price'),
                'img_name': upload_image(request.files['product_image'])
            }
            save_data("blueprints/products/products.json", data)
            return redirect('/product')
    return render_template('add_product.html', form=form)
