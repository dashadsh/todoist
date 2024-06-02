```
pip install django
pip install djangorestframework
```

create new "todoproject"
```
django-admin startproject todoproject
cd todoproject
```
Creates a Directory: It creates a directory named todoproject.
Creates Subdirectories and Files: Inside todoproject, it creates the following structure:

todoproject/  
    manage.py  
    todoproject/  
        __init__.py  
        settings.py  
        urls.py  
        wsgi.py  

**manage.py:** A command-line utility that lets you interact with this Django project. You’ll use it to run commands like runserver, migrate, and startapp.  
**init.py:** An empty file that tells Python this directory should be considered a Python package.  
**settings.py:** Contains all the configuration for your Django project.  
**urls.py:** The URL declarations for this Django project; a “table of contents” of your Django-powered site.  
**wsgi.py:** An entry-point for WSGI-compatible web servers to serve your project.  


Inside the project directory, create a new app called todo:
```
python3 manage.py startapp todo
```

It will create: 
todo/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py

```
nano todoproject/setting.py
```
```
nano todo/models.py
```
```
python manage.py makemigrations
python manage.py migrate
```
```
touch todo/serializers.py
nano todo/serializers.py
```
```
edit todo/views.py
```
```
touch todo/urls.py
nano todo/urls.py
```
```
mkdir todo/templates
touch todo/templates/index.html
nano todo/templates/index.html
```
```
python3 manage.py runserver
```
