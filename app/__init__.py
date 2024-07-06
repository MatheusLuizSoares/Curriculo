import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'chave1'
    app.config['UPLOAD_FOLDER'] = 'app/uploads'
    app.config['MAX_CONTENT_PATH'] = 1 * 1024 * 1024  # 1MB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///curriculos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    with app.app_context():
        from . import routes, models
        db.create_all()

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    return app
