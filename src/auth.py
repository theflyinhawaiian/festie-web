from flask import Blueprint, request, jsonify
from src.extensions import db, bcrypt
from src.model.user import User
from src.model.auth_token import AuthToken

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def register():
    user_email = request.form.get("email")
    
    if(User.query.filter_by(email=user_email).first()):
        return "User with email already exists", 400

    user = User(request.form.get("email"), request.form.get("password"))
    db.session.add(user)
    db.session.commit()

    return f"User {user.email} created!", 200

@auth.route("/login", methods=["POST"])
def login():
    user_email = request.form.get("email")

    user = User.query.filter_by(email=user_email).first()

    if(not bcrypt.check_password_hash(user.password, request.form.get("password"))):
        return "Bad username/password combination", 401

    token = AuthToken.encode_token(user.id)
    print(f"Issued token: {token[0]}")

    return jsonify({
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': token
                }), 200

@auth.route("/logout", methods=["POST"])
def logout():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        token = ''
    if token:
        resp = AuthToken.decode_token(token)
        if not isinstance(resp, str):
            user = User.query.filter_by(id=resp).first()
            if user:
            # mark the token as blacklisted
            # blacklist_token = BlacklistToken(token=auth_token)
            # # try:
            #     insert the token
            #     db.session.add(blacklist_token)
            #     db.session.commit()
            #     responseObject = {
            #         'status': 'success',
            #         'message': 'Successfully logged out.'
            #     }
            #     return jsonify(responseObject), 200
            # except Exception as e:
            #     responseObject = {
            #         'status': 'fail',
            #         'message': e
            #     }
            #     return jsonify(responseObject), 401
                return jsonify({"logged_out" : True }), 200
            else:
                return jsonify(resp), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': resp
            }
            return jsonify(responseObject), 401
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Provide a valid auth token.'
        }
        return jsonify(responseObject), 403
