from flask_restful import Resource
#from models.models import RoomsModel


class Rooms(Resource):

    def get(self):
        return "GET" #RoomsModel.query.all()

    def post(self):
        return "POST"

    def put(self):
        return "PUT"

    def delete(self):
        return "DELETE"
