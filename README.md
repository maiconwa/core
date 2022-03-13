# core

API with Django REST Framework.
<br>
In order to use this software some steps are required:
<br>
1 - Create a virtual environment using python3 -m venv venv.
<br>
2 - Activate the virtual environment in /core/venv/bin. Command: source activate.
<br>
3 - Install pip requirements.txt in /core/core. Command: pip install -r requirements.txt.
<br>
4 - Run commands: python3 manage.py makemigrations followed by python3 manage.py migrate to create the sqlite database.
<br>
5 - Create a superuser for django admin. Command: python3 manage.py createsuperuser
<br>
6 - Run the application. Command: python3 manage.py runserver
<br>
7 - Using the web browser, type http://127.0.0.1:8000/ or http://localhost:8000/ to see API Root.
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
