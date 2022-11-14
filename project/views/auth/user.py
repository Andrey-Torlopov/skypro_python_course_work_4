from flask_restx import Namespace, Resource

from flask import request, abort

from project.container import user_service
from project.tools.security import auth_required, get_email_from_token
from project.dao.model.user import UserScheme

api = Namespace('user')

@api.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        email = get_email_from_token(token)
        model = user_service.get_user_by_email(email)
        if model is None:
            abort(404, "User not found")

        return UserScheme().dump(model), 200


    @auth_required
    def patch(self):
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        email = get_email_from_token(token)
        model = user_service.get_user_by_email(email)
        if model is None:
            abort(404, "User not found")

        data = request.json
        data['id'] = model.id
        user_service.patch(data)
        return "", 201


@api.route('/password/')
class PasswordView(Resource):
    @auth_required
    def put(self):
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        email = get_email_from_token(token)
        model = user_service.get_user_by_email(email)
        if model is None:
            abort(404, "User not found")

        data = request.json
        data['id'] = model.id
        # user_service.update_password(data)
        print("...")
        return "", 201
