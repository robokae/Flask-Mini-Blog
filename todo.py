import os
from app import create_app, db
from app.models import User
from flask_migrate import Migrate

app = create_app()          # call the application factory
migrate = Migrate(app, db)