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
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///curriculos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_SERVER'] = 'smtp.example.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'seu-email@example.com'
    app.config['MAIL_PASSWORD'] = 'sua-senha'

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    with app.app_context():
        from . import routes, models
        db.create_all()

    return app
