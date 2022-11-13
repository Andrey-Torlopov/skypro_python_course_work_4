from project.setup.db import models, db
from marshmallow import Schema, fields


class Director(models.Base):
    __tablename__ = 'director'

    name = db.Column(db.String(100), unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
