import re
import os
from notificacoes.models import Email
from eventos.models import Evento

class EmailHelper:

	URL = os.environ['API_URL']
	
	@staticmethod
	def email_convite(self):
		conteudo = '''
			<html>
				<head></head>
				<body>
					<p>Olá, <b>nome_convidado!</b> Como vai?<br>

					<p><b>Você foi convidado para o evento:</b> descricao_evento</p>
					<p><b>Data</b>: data_evento</p>

					Clique no link para confimar a sua presença: <a href="url_api/convidados/id_convidado/confirmarpresenca">Confirmar</a>.
					</p>
				</body>
			</html>
		'''
		conteudo = re.sub(r'nome_convidado', self.nome, conteudo)
		conteudo = re.sub(r'id_convidado', str(self.id), conteudo)
		conteudo = re.sub(r'descricao_evento', self.evento.descricao, conteudo)
		conteudo = re.sub(r'data_evento', str(self.evento.data_hora), conteudo)
		conteudo = re.sub(r'url_api', EmailHelper.URL, conteudo)

		email = Email(self.e_mail, "[Convite para Evento]", str(conteudo))
		email.enviar()
	
	@staticmethod
	def email_convidado_confirmado(self):
		conteudo = '''
			<html>
				<head></head>
				<body>
					<p>Olá, <b>responsavel_evento!</b> Como vai?<br>

					<p><b>O convidado:</b> nome_convidado</p>
					<p><b>Confirmou presença para o evento:</b> descricao_evento</p>
					<p><b>Date e Hora:</b> data_hora</p>
				</body>
			</html>
		'''

		conteudo = re.sub(r'responsavel_evento', str(self.evento.responsavel), conteudo)
		conteudo = re.sub(r'nome_convidado', self.nome, conteudo)
		conteudo = re.sub(r'descricao_evento', self.evento.descricao, conteudo)
		conteudo = re.sub(r'data_hora', str(self.evento.data_hora), conteudo)

		email = Email(self.e_mail, "[Confirmação de Presença]", str(conteudo))
		email.enviar()
		
