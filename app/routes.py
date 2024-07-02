from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import CurriculoForm
from werkzeug.utils import secure_filename
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curriculo', methods=['GET', 'POST'])
def curriculo():
    form = CurriculoForm()
    if form.validate_on_submit():
        arquivo = form.arquivo.data
        filename = secure_filename(arquivo.filename)
        arquivo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        arquivo.save(arquivo_path)
        
        flash('Currículo enviado com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('curriculo.html', form=form)
