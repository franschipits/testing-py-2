from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)

def create_game(name, description):
    """Create and return a new game."""

    game = Game(name=name, description=description)

    return game

def example_data():
    """Create example data for the test database."""

    test_game1 = create_game("testGame1", "testDescription1")
    test_game2 = create_game("testGame2", "testDescription2")

    db.session.add(test_game1)
    db.session.add(test_game2)
    db.session.commit()

if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
