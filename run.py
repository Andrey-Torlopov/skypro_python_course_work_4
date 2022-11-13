from project.config import config
from project.dao.model.genre import Genre
from project.dao.model.director import Director
from project.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director
    }
