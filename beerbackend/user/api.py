from beerbackend.user.models import User
from flask_restful import Resource, reqparse


auth_parse = reqparse.RequestParser()
auth_parse.add_argument('username', dest='username',
                        type=str, required=True,
                        help='username of user to authenticate and gather a token for')

auth_parse.add_argument('password', dest='password',
                        type=str, required=True,
                        help='password of user to authenticate and gather a token for')
class AuthApi(Resource):
    def get(self):
        args = auth_parse.parse_args()
        username = args.username
        password = args.password
        user = User.query.filter(User.username == username).first()
        if user and user.check_password(password):
            return {'access_token': user.generate_auth_token()}

        else:
            return None, 401

recommend_get_parse = reqparse.RequestParser()
recommend_get_parse.add_argument('access_token', dest='access_token',
                                 type=str, required=True,
                                 help='The access_token of the user you want a recommend')


class UserApi(Resource):
    def get(self):
        args = recommend_get_parse.parse_args()
        user = User.verify_auth_token(args.access_token)
        if user:
            #this won't return this in the future, placeholder.
            return {"username": user.username}

