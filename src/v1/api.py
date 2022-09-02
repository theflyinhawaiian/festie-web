from flask import Blueprint, jsonify
from flask_restx import Api, Resource

api_v1 = Blueprint('api_v1', __name__)
api = Api(api_v1)

@api.route('/festivals')
class Festivals(Resource):
    def get(self):
        return jsonify({ "Festivals" : ["Firefly", "Bonnaroo", "EDC", "Lollapalooza", "Coachella"] })

@api.route('/festival')
class Festival(Resource):
    def get(self, id):
        return jsonify({ "Artists" : ["Bleachers", "Wreckno", "Zedd", "Yellowcard", "Madeon", "Anderson.Paak"] })

@api.route('/artist')
class Artists(Resource):
    def get(self, id):
        return jsonify({ 
            "id" : 1234,
            "tracks" : ["track1" , "track2", "track3", "track4"]
         })