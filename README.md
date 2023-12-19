# Cadastro de Produtos e Api de Estoque

## Este projeto foi feito com:

* [Python 3.11](https://www.python.org/)
* [Django 4.2.6](https://www.djangoproject.com/)
* [Django-Ninja](https://django-ninja.rest-framework.com/)
* [AlpineJS](https://alpinejs.dev/)


### Web API usando Django Ninja para consumo de dados de produtos

Para instalar o projeto execute os seguintes passos.

```bash
git clone https://github.com/djwesleyborges/product-app.git
cd product-app

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py loaddata application_data.json
python manage.py runserver
```
Projeto: http://127.0.0.1:8000/ 

http://localhost:8000/admin </br>
user: admin </br>
pass: admin </br>

Api: http://localhost:8000/api/docs