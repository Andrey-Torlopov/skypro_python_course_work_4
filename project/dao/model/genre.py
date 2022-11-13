from project.setup.db import models, db
from marshmallow import Schema, fields


class Genre(models.Base):
    __tablename__ = 'genre'

    name = db.Column(db.String(100), unique=True, nullable=False)


class GenreScheme(Schema):
    id = fields.Int()
    name = fields.Str()
