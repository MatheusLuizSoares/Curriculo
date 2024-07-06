from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class CurriculoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    telefone = StringField('Telefone', validators=[DataRequired(), Length(max=20)])
    cargo_desejado = StringField('Cargo Desejado', validators=[DataRequired(), Length(max=100)])
    escolaridade = SelectField('Escolaridade', choices=[
        ('fundamental', 'Ensino Fundamental'),
        ('medio', 'Ensino Médio'),
        ('superior', 'Ensino Superior')
    ], validators=[DataRequired()])
    observacoes = TextAreaField('Observações')
    arquivo = FileField('Arquivo', validators=[FileRequired(), FileAllowed(['pdf', 'doc', 'docx'], 'Apenas arquivos PDF, DOC e DOCX são permitidos.')])
