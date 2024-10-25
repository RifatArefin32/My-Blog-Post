# Setup the Project
- Create a directory `DjangoBlogPost` at Desktop or any other directory and enter into the `DjangoBlogPost` directory.
- Create a virtual environment `venv` for this project using `python -m venv venv` command.
- Activate the virtual environment using `source venv/bin/activate` command and deactivate it using `deactivate` command.
- Install django at this environment `pip3 install django`
- Install Django REST Framework at this environment `pip3 install djangorestframework`
- Create project: `django-admin startproject myblog_project` and enter into the porject.
- Start the porject at the server: `python3 manage.py runserver`
- Add rest-framework at the INSTALLED_APPS array of the project settings file.
- Add `path('api-auth/', include('rest_framework.urls')),` to the project urls file

# Connect PostgreSQL database
- Install PostgreSQL to the PC (if not installed)
- Open postgresql from the terminal using `sudo -u postgres psql` command
- Create a database and a user for this project, then grant all privileges
```
CREATE DATABASE your_database_name;
CREATE USER your_username WITH PASSWORD 'your_password';
ALTER ROLE your_username SET client_encoding TO 'utf8';
ALTER ROLE your_username SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_username SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;
```
- Install psycopg2 or psycopg: Activate the virtual environment and try installing `psycopg2-binary` instead of `psycopg2`, as it’s easier to install and suitable for development using `pip install psycopg2-binary` command.
- In our Django project’s `settings.py`, configure the database settings like this:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',  # Set to empty string for localhost
        'PORT': '5432',       # Default PostgreSQL port
    }
}
```
- Run migration from the project directory using `python3 manage.py migrate` command
- Create a super user using `python3 manage.py createsuperuser`. This super user is treated as `admin`.


# Add Authentication using Simple-JWT
[Documentation of simple-jwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
- Install Django Rest Framework's simple-jwt using `pip install djangorestframework-simplejwt` command
- Add `'rest_framework_simplejwt',` to the INSTALLED_APPS array
- Create `mbp_authentication` app and register it into the INSTALLED_APPS array
- Add the following snippet to the `settings.py` file
```
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        )
    }
``` 
- Add and create classes in `serializers.py` at the `mbp_authentication` app
- Create `RegisterView` class at the `views.py` file