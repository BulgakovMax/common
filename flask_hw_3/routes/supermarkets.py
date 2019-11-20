import json

from flask import Blueprint, Response, request
from model import Supermarkets

supermarket = Blueprint('supermarket', __name__)


@supermarket.route('/supermarket', methods=['GET'])
def get_tables():
    result = [{'id': supermarket.id, 'name': supermarket.name, 'location': supermarket.location,
               'img_name': supermarket.img_name} for table in DB['table']]
    data = json.dumps(result)
    return Response(data, status=200)


@supermarket.route('/supermarket', methods=['POST'])
def restaurants_create():
    data = request.json
    DB['supermarkets'].append(Supermarkets(data['number'], data['guest_count']))
    return Response(status=200)
