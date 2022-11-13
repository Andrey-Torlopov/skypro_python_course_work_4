from flask_restx import Namespace, Resource

from project.container import director_service as service
from project.setup.api.models import director
from project.setup.api.parsers import page_parser
from project.dao.model.director import DirectorSchema

api = Namespace('directors')


@api.route('/')
class DirectorsView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(director, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all directors.
        """
        models = service.get_all(**page_parser.parse_args())
        res = DirectorSchema(many=True).dump(models)
        return res, 200


@api.route('/<int:uid>/')
class DirectorView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(director, code=200, description='OK')
    def get(self, uid: int):
        """
        Get director by id.
        """
        model = service.get_item(uid)
        res = DirectorSchema().dump(model)
        return res, 200
