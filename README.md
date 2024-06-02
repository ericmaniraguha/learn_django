# Django Learning Project

## Overview

This project is a simple Django application designed to help you learn the basics of Django, including setting up a project, creating views, and routing URLs. The project includes a main app called `playground` with a couple of example views.

## Key Features of Django

1. **The Admin Site**

   - Built-in admin interface to manage database models.
   - Highly customizable and extendable.

2. **Object-Relational Mapper (ORM)**

   - Interact with the database using Python code.
   - Supports multiple database backends like PostgreSQL, MySQL, SQLite, and Oracle.

3. **Authentication**

   - Robust authentication system handling user accounts, groups, permissions, and sessions.
   - Includes views and forms for logging in, logging out, and password management.

4. **Caching**
   - Caching framework to speed up the website by storing frequently accessed data in memory.
   - Supports various cache backends, including Memcached, Redis, and database caching.

## Setup Instructions

### 1. Start a New Django Project

```bash
django-admin startproject storefront .
```

### 2. Run the development server

`python manage.py runserver 9000`

This command starts the Django development server on `port 9000`. Access your project at `http://127.0.0.1:9000/`.

### 3. Create a new Apps.

`python manage.py startapp playground`

This command creates a new app named `playground` within your Django project.

### 4. Set Up Your Virtual Environment and Install Dependencies

`Navigate to your project directory (if not already there)`
`cd /e/django/django-tutorial-mosh`

#### Activate the virtual environment

`source django-env/Scripts/activate`

#### Set the environment variable

`export django-env=development`

Optionally, make the environment variable persistent by adding it to `~/.bashrc or ~/.bash_profile`

`echo 'export django-env=development' >> ~/.bashrc`
`source ~/.bashrc  # or source ~/.bash_profile`

#### Install Django

`pip install django`

#### Install all packages listed in `requirements.txt`

`pip install -r requirements.txt`

#### Verify the environment variable

`echo $django-env`

##### Writing Views

In Django, a view is a Python function that receives a web request and returns a web response. Views are defined in the `views.py` file of your app.

##### Example Views

`playground/views.py`

```python
from django.http import HttpResponse

def say_hello(request):
return HttpResponse("Hello, Django!")

def home(request):
return HttpResponse("Welcome to the homepage!")`
```

##### Mapping Views to URLs

To map a view to a URL, define URL patterns in the `urls.py` file of your app or project.

`playground/urls.py`

```python
from django.urls import path
from . import views

###### URLConf

urlpatterns = [
    path('hello/', views.say_hello, name='hello'),
    path('', views.home, name='home'), # Root URL
]
```

`storefront/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

# Main URL configurations
urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('', include('playground.urls')),  # Include the playground URLs for the root path
]

```

#### Request-Response Cycle

1. **Request:** The client (e.g., web browser) sends an HTTP request to the server.
2. **Handler:** Django routes the request to the appropriate view function based on the URL.
3. **Action:** The view function processes the request, potentially interacting with the database or other services.
4. **Response:** The view function returns an HTTP response to the client.

## Running the Application

Ensure your virtual environment is activated.

Run the development server with:

```bash
python manage.py runserver 9000
```

##### Open your browser and navigate to:

`http://127.0.0.1:9000/` to see "Welcome to the homepage!"
`http://127.0.0.1:9000/playground/hello/` to see "Hello, Django!"

##### Conclusion

This project serves as a starting point for learning Django. It demonstrates setting up a Django project, creating views, and routing URLs. You can expand this project by adding more apps, models, and views as you continue learning Django.
