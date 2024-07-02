from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FileField, ValidationError
from wtforms.validators import DataRequired, Email

def validacao_arquivo_extensao(form, field):
    allowed_extensions = ['doc', 'docx', 'pdf']
    if not field.data.filename.split('.')[-1] in allowed_extensions:
        raise ValidationError('Extensão de arquivo não permitida. As extensões permitidas são: doc, docx, pdf.')

class CurriculoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    cargo_desejado = StringField('Cargo Desejado', validators=[DataRequired()])
    escolaridade = SelectField('Escolaridade', choices=[
        ('fundamental', 'Ensino Fundamental'),
        ('medio', 'Ensino Médio'),
        ('superior', 'Ensino Superior')
    ], validators=[DataRequired()])
    observacoes = TextAreaField('Observações')
    arquivo = FileField('Arquivo', validators=[DataRequired(), validacao_arquivo_extensao])
