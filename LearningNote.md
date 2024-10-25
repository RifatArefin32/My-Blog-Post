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
- Run migration from the project directory using `python3 manage.py migrate` command
- Create a super user using `python3 manage.py createsuperadmin`. This super user is treated as `admin`.


# Add Authentication using Simple-JWT
[Documentation of simple-jwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)
- Install DjangoRestFramework's simple-jwt using `pip install djangorestframework-simplejwt` command
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
- Add `serializers.py` at the `mbp_authentication` app