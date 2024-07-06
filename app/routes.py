from flask import render_template, flash, redirect, url_for, request, current_app as app
from . import db
from .forms import CurriculoForm
from .models import Curriculo
from .utils import enviar_email 
from werkzeug.utils import secure_filename
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curriculo', methods=['GET', 'POST'])
def curriculo():
    form = CurriculoForm()
    if form.validate_on_submit():
        filename = None
        if form.arquivo.data:
            arquivo = form.arquivo.data
            filename = secure_filename(arquivo.filename)
            arquivo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                arquivo.save(arquivo_path)
                app.logger.info(f"Arquivo salvo em: {arquivo_path}")
            except Exception as e:
                app.logger.error(f"Erro ao salvar o arquivo: {e}")
                flash('Erro ao salvar o arquivo.', 'danger')
                return redirect(url_for('curriculo'))
        else:
            app.logger.warning("Nenhum arquivo foi carregado.")

        curriculo = Curriculo(
            nome=form.nome.data,
            email=form.email.data,
            telefone=form.telefone.data,
            cargo_desejado=form.cargo_desejado.data,
            escolaridade=form.escolaridade.data,
            observacoes=form.observacoes.data,
            arquivo=filename,
            ip=request.remote_addr
        )
        db.session.add(curriculo)
        db.session.commit()

        try:
            enviar_email(curriculo.nome, curriculo.email, curriculo.telefone, curriculo.cargo_desejado, 
                         curriculo.escolaridade, curriculo.observacoes, arquivo_path)
            flash('Currículo enviado com sucesso!', 'success')
        except Exception as e:
            app.logger.error(f"Erro ao enviar o e-mail: {e}")
            flash('Erro ao enviar o e-mail.', 'danger')

        return redirect(url_for('curriculo'))

    return render_template('curriculo.html', form=form)
