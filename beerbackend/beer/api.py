from beerbackend.beer.models import Beer
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask.json import jsonify


get_parse = reqparse.RequestParser()
get_parse.add_argument('name', dest='name',
                       type=str, required=True,
                       help='The Name of the beer')

class BeerApi(Resource):
    def get(self):
        args = get_parse.parse_args()
        name = args.name
        beer = Beer.query.filter(Beer.beer_name == name).first()
        print(name)
        print(beer)
        if beer:
            return beer.to_data()
        else:
            return None
