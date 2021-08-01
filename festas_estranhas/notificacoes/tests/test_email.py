from notificacoes.models import Email

class TestModels:
	
	def test_email(self):
		email = Email('fernando.gmp@gmail.com', "[Convite para Evento]", "<h1>Testing..</h1>")
		response = email.enviar()
