from flask import render_template, flash, redirect, url_for, request, current_app as app
from . import db, mail
from .forms import CurriculoForm
from .models import Curriculo
from flask_mail import Message
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
            arquivo=filename,  # Salvar o nome do arquivo no banco de dados
            ip=request.remote_addr
        )
        db.session.add(curriculo)
        db.session.commit()

        # Enviar e-mail com os dados do formulário
        msg = Message('Novo Currículo Enviado',
                      sender='seu-email@example.com',
                      recipients=['teste@teste.com'])  # Usando o e-mail fake para testes
        msg.body = f'''
        Nome: {curriculo.nome}
        E-mail: {curriculo.email}
        Telefone: {curriculo.telefone}
        Cargo Desejado: {curriculo.cargo_desejado}
        Escolaridade: {curriculo.escolaridade}
        Observações: {curriculo.observacoes}
        IP: {curriculo.ip}
        Data de Envio: {curriculo.data_envio}
        '''
        if filename:
            try:
                with app.open_resource(arquivo_path) as fp:
                    msg.attach(filename, "application/octet-stream", fp.read())
            except Exception as e:
                app.logger.error(f"Erro ao anexar o arquivo no e-mail: {e}")
        try:
            mail.send(msg)
        except Exception as e:
            app.logger.error(f"Erro ao enviar o e-mail: {e}")
            flash('Erro ao enviar o e-mail.', 'danger')
            return redirect(url_for('curriculo'))

        flash('Currículo enviado com sucesso!', 'success')
        return redirect(url_for('curriculo'))
    
    return render_template('curriculo.html', form=form)
