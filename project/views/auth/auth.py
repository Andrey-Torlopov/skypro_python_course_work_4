from flask_restx import Namespace, Resource
from flask import request, abort

from project.container import auth_service
from project.container import user_service


api = Namespace('auth')

@api.route('/login/')
class LoginView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get('email')
        password = req_json.get('password')
        if None in [email, password]:
            abort(401)

        return auth_service.auth_user(email, password)

    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token')
        if refresh_token is None:
            abort(401)

        tokens = auth_service.refresh_token(refresh_token)

        return tokens, 201


@api.route('/register/')
class RegisterView(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if None in [email, password]:
            abort(400)

        user_service.create(data)

        tokens = auth_service.auth_user(email=email, password=password)

        if not tokens:
            return {"error": "Ошибка в логине или пароле"} , 401

        return tokens, 201
