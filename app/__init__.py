from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

# application factory
def create_app():
    app = Flask(__name__)

    # get config
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # routes from blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app