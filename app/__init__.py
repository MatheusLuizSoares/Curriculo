from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave1'
app.config['UPLOAD_FOLDER'] = 'uploads' 
from app import routes
