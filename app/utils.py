import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def enviar_email(nome, email, telefone, cargo_desejado, escolaridade, observacoes, filepath):
    fromaddr = "teste@teste.com"
    toaddr = "teste@teste.com"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Novo Currículo Enviado"
    
    body = f"""
    Nome: {nome}
    E-mail: {email}
    Telefone: {telefone}
    Cargo Desejado: {cargo_desejado}
    Escolaridade: {escolaridade}
    Observações: {observacoes}
    """
    
    msg.attach(MIMEText(body, 'plain'))

    try:
        attachment = open(filepath, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(filepath)}")
        msg.attach(part)
    except Exception as e:
        print(f"Erro ao anexar o arquivo: {e}")

   
    try:
        server = smtplib.SMTP('localhost')
        server.sendmail(fromaddr, toaddr, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")
