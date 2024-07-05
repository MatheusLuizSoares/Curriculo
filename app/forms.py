# app/forms.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SelectField, StringField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Email

class CurriculoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    cargo_desejado = StringField('Cargo Desejado', validators=[DataRequired()])
    escolaridade = SelectField('Escolaridade', choices=[
        ('fundamental', 'Ensino Fundamental'),
        ('medio', 'Ensino Médio'),
        ('superior', 'Ensino Superior')
    ],)
    observacoes = TextAreaField('Observações')
    arquivo = FileField('Arquivo', validators=[FileAllowed(['pdf', 'doc', 'docx'], 'Apenas arquivos PDF, DOC e DOCX são permitidos.')])

    def validacao_arquivo_extensao(self, field):
        if field.data:
            if not field.data.filename.split('.')[-1] in ['pdf', 'doc', 'docx']:
                raise ValidationError('Extensão de arquivo não permitida!')
