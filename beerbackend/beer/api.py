from beerbackend.beer.models import Beer
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask.json import jsonify


beer_get_parse = reqparse.RequestParser()
beer_get_parse.add_argument('beer_name', dest='beer_name',
                       type=str, required=True,
                       help='The Name of the beer')

PBR = {
  "sour": 1,
  "malty": 1,
  "family": "pale-lager",
  "hoppy": 1,
  "name": "PBR",
  "abv": 1,
  "wood": 1,
  "bitter": 1,
  "color": 1,
  "roasty": 1,
  "spice": 1,
  "sweet": 1,
  "fruit": 1
}


class BeerApi(Resource):
    def get(self):
        args = beer_get_parse.parse_args()
        name = args.beer_name
        beer = Beer.query.filter(Beer.beer_name == name).first()
        print(name)
        print(beer)
        if beer:
            return beer.to_data()
        else:
            return None

class BeersApi(Resource):
    def get(self):
        beers = Beer.query.all()
        if beers:
            return{"beers": [beer.to_data() for beer in beers]}
        else:
            return {"beers": []}
