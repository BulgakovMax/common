import json
import logging
import os


def get_data(filename):
    try:
        with open(filename) as json_file:
            return json.load(json_file)
    except ValueError:
        logging.critical("File 'products.json' contains not valid data")
    except FileNotFoundError:
        logging.critical("File 'products.json' not found")


def add_data(data, new_data):
    try:
        with open(new_data, mode='w') as file:
            return json.dump(data, file)
    except ValueError:
        return new_data


def upload_image(request_files):
    if request_files:
        image = request_files
        image.save(os.path.join('blueprints/products/static', image.filename))
        return image.filename
    else:
        return 'no_image.jpg'


def save_data(data_file, data):
    items_list = get_data(data_file)
    data = data
    items_list.append(data)
    add_data(items_list, data_file)
