import json

from flask import Blueprint, Response, request
from model import Products

product = Blueprint('product', __name__)


@product.route('/product', methods=['GET'])
def get_product():
    result = [{'id': product.id, 'name': product.name, 'description': product.description,
               'img_name': product.img_name, 'price': product.price} for table in DB['table']]
    data = json.dumps(result)
    return Response(data, status=200)


@product.route('/product', methods=['POST'])
def create_product():
    data = request.json
    DB['products'].append(Products(data['number'], data['guest_count']))
    return Response(status=200)
