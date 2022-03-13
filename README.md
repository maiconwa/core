# core

API with Django REST Framework.
<br>
In order to use this software some steps are required:
<br>
Advise: Some of the following commands may differ if you are using a diferent system, the commands ahead were used in a linux ubuntu machine.
<br>
1 - Create a virtual environment using python3 -m venv venv.
<br>
2 - Activate the virtual environment at /core/venv/bin. Command: source activate.
<br>
3 - Install pip requirements.txt at /core/core. Command: pip install -r requirements.txt.
<br>
4 - Generate a secret_key for django. Command: python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
<br>
5 - Create a file named ticket.py inside core project. Add a variable named ticket and add the secret key as the following: ticket = 'your secret_key must be placed here'.
<br>
6 - Run commands: python3 manage.py makemigrations followed by python3 manage.py migrate to create the sqlite database.
<br>
7 - Create a superuser for django admin. Command: python3 manage.py createsuperuser
<br>
8 - Run the application. Command: python3 manage.py runserver
<br>
9 - Using the web browser, type http://127.0.0.1:8000/ or http://localhost:8000/ to see API Root.
<p>
</p>
<br>
API Root:
<br>
<img src=https://github.com/maiconwa/core/blob/main/core/images/Root1.png>
<p>
</p>
<br>
API Livros:
<br>
<img src=https://github.com/maiconwa/core/blob/main/core/images/Livros.png>
<br>
API Jogos:
<br>
<img src=https://github.com/maiconwa/core/blob/main/core/images/Jogos.png>
<br>