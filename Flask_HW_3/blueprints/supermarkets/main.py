import uuid

from flask import Blueprint, render_template, request, url_for, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, validators, FloatField
from wtforms.validators import DataRequired
from utils import get_data, save_data, upload_image

supermarket = Blueprint('supermarket',
                        __name__,
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='/supermarkets/static'
                        )


class AddSupermarketForm(FlaskForm):
    supermarket_name = StringField('Name of supermarket:', validators=[DataRequired()])
    supermarket_location = TextAreaField('Location of supermarket:', validators=[DataRequired()])
    supermarket_image = FileField()
    submit = SubmitField('Add supermarket')


@supermarket.route('/supermarket', methods=['GET'])
def get_all_supermarkets():
    list_of_supermarkets = get_data("blueprints/supermarkets/supermarkets.json")
    if request.args.getlist('location'):
        filtered_data = []
        for supermarket in list_of_supermarkets:
            if supermarket['location'] == request.args.getlist('location')[0]:
                filtered_data.append(supermarket)
        return render_template('all_supermarkets.html',
                               title='Supermarkets',
                               list_of_supermarkets=filtered_data,
                               )
    else:
        return render_template('all_supermarkets.html',
                               title='Supermarkets',
                               list_of_supermarkets=list_of_supermarkets,
                               )


@supermarket.route('/supermarket/<super_id>', methods=['GET'])
def get_supermarket(super_id):
    list_of_supermarkets = get_data("blueprints/supermarkets/supermarkets.json")
    for supermarket in list_of_supermarkets:
        if supermarket['id'] == super_id:
            session[super_id + supermarket['name']] = 'visited'
            return render_template(
                'supermarket.html',
                name=supermarket['name'],
                location=supermarket['location'],
                img_name=supermarket['img_name']
            )
    else:
        return render_template(url_for('404.html'))


@supermarket.route('/add_supermarket', methods=['GET', 'POST'])
def add_supermarket():
    form = AddSupermarketForm()
    supermarket_list = get_data("blueprints/supermarkets/supermarkets.json")
    supermarket_id = str(uuid.uuid4())
    if request.method == 'POST':
        if form.validate_on_submit():
            data = {
                'id': supermarket_id,
                'name': request.form.get('supermarket_name'),
                'location': request.form.get('supermarket_location'),
                'img_name': upload_image(request.files['supermarket_image'])
            }
            save_data("blueprints/supermarkets/supermarkets.json", data)
            return redirect('/supermarket')
    return render_template('add_supermarket.html', form=form)
