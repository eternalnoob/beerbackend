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
    def post(self):
        create_user_parse = reqparse.RequestParser()
        create_user_parse.add_argument('username', dest='username',
                                       required=True,
                                       help="Username of user to be created")
        create_user_parse.add_argument('password', dest='password',
                                       required=True,
                                       help="Password of user to be created")
        create_user_parse.add_argument('password_confirm', dest='password_confirm',
                                       required=True,
                                       help="Password confirmation of user to be created")
        create_user_parse.add_argument('email', dest='email',
                                       required=True,
                                       help="Email address of user to be created")
        args = create_user_parse.parse_args()

        user = User.query.filter(User.username == args.username).first()
        emailuser = User.query.filter(User.email == args.email).first()
        if user:
            return {"message": "username already exists"}, 400
        elif emailuser:
            return {"message": "email already registered"}, 400
        elif args.password != args.password_confirm:
            return {"message": "passwords do not match"}, 400
        elif len(args.password) < 6 or len(args.password) > 128:
            return {"message": "invalid password length"}, 400
        elif not args.username or len(args.username) > 80:
            return {"message": "invalid username length"}, 400
        else:
            valid_user = User.create(username=args.username, password=args.password,
                                     email=args.email, active=True)
            return {"message": "User {} created successfully".format(args.username)}

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

class UserBeers(Resource):
    def get(self):
        args = recommend_get_parse.parse_args()
        user = User.verify_auth_token(args.access_token)
        if user:
            #this won't return this in the future, placeholder.
            return {"beers": [{"beer": PBR, "rating": 2},
                              {"beer": PBR, "rating": 3}],
                    "total": 2,
                    }

