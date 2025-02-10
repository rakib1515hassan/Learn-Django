1) Create a Vertual Environment
    >> py -m venv <env>

2) Activate the environment
    >> env\scripts\activate

3) Check the environment for any library
    >> pip freeze

4) Install Django
    >> pip install django

5) Update pip version
    >> python.exe -m pip install --upgrade pip

6) Listout the packages from environment
    >> pip freeze > requirements.txt

7) Install all packages from requirements.txt file
    >> pip install -r requirements.txt

8) Create a New Django Project
    >> django-admin startproject <core> .

9) Apps Create a new Django Project
    >> py manage.py startapp <apps>

10) Migrations
    >> py manage.py makemigrations
    
11) Migrate
    >> py manage.py migrate

12) Create a Superadmin
    >> py manage.py createsuperuser

13) Surver Run
    >> py manage.py runserver