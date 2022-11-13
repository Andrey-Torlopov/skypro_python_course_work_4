from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Директор', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Название 1'),
})

movie: Model = api.model('Кино', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Название 1'),
    'trailer': fields.String(required=True, max_length=100, example='Trailer 1'),
    'year': fields.Integer(required=True, example=2000),
    'rating': fields.String(required=True, max_length=100, example='R'),
    'genre_id': fields.Integer(required=True, example=1),
    'director_id': fields.Integer(required=True, example=1),
})