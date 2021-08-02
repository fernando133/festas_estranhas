# API Festas Estranhas
Django Rest Framework API

## Installation

### Instalando dependências:

```apt-get install pipenv```

No folder da aplicação rodar o seguinte:
   
 ```pipenv shell```
 ```pipenv install```

### Rodando migrations
```python manage.py makemigrations```
```python manage.py migrate```

### Variáveis de Ambeinte Utilizadas

export API_URL=http://127.0.0.1:8000
export SMTP_SERVER=smtp.gmail.com
export SMTP_PORT=587
export SENDER_EMAIL=
export SENDER_PASSWORD=

### Starting
```python manage.py runserver 0.0.0.0:8000```

## Postman collection para auxilar no uso de autenticação e testes de requisições
https://www.getpostman.com/collections/e1650a9a2f05410d425c

## Link acesso servidor de testes / admin
- http://143.244.169.149:8000
- http://143.244.169.149:8000/admin
- Login: admin
- Senha: admin
