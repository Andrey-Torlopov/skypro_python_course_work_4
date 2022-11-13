from flask_restx import Namespace, Resource
from flask import abort, request

from project.container import movie_service as service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser
from project.dao.model.movie import MovieScheme

from project.tools.security import auth_required

api = Namespace('movies')


@api.route('/')
class MoviesView(Resource):
    @auth_required
    @api.expect(page_parser)
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all movies.
        """
        # data = {
        #     'status': request.args.get('status'),
        #     'page': request.args.get('page')
        # }

        models = service.get_all()
        return MovieScheme(many=True).dump(models), 200


@api.route('/<int:movie_id>/')
class MovieView(Resource):
    @auth_required
    @api.response(404, 'Not Found')
    @api.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        try:
            model = service.get_item(movie_id)
            return MovieScheme().dump(model), 200
        except Exception as e:
            abort(404, message="Movie not found")
