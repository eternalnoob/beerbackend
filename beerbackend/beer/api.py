from beerbackend.beer.models import Beer
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask.json import jsonify
from ..user.models import User


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

recommend_get_parse = reqparse.RequestParser()
recommend_get_parse.add_argument('access_token', dest='access_token',
                       type=str, required=True,
                       help='The access_token of the user you want a recommend')


class Recommend(Resource):
    def get(self):
        args = recommend_get_parse.parse_args()
        user = User.verify_auth_token(args.access_token)
        if user:
        #lol for now
            return PBR
        else:
            return None, 401
