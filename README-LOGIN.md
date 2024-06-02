## Django Login Project

##### This is a simple Django project demonstrating basic login functionality.

1. Setup Instructions
2. Install Dependencies

```python

python -m venv django-env
source django-env/bin/activate  # On Windows, use `django-env\Scripts\activate`
pip install django

```

3. Create and Apply Migrations

```python

python manage.py makemigrations
python.manage.py migrate
```

4. Run the server

```python
python manage.py runserver 9000
```

5. Access the Application
   Visit `http://127.0.0.1:9000/`.

6. Default Credentials
   Username: `ericmaniraguha`
   Password: `password`

7. File Overview

`playground/views.py`

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
    if not User.objects.filter(username='ericmaniraguha').exists():
        User.objects.create_user(username='ericmaniraguha', password='password')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success')
        else:
            return redirect('login_error')
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')

def login_error(request):
    return render(request, 'login_error.html')

```

`playground/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('login_error/', views.login_error, name='login_error'),
]
```

`storefront/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('playground.urls')),
]

```

`playground/templates/index.html`

```python
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f2f2f2; }
        .login-container { display: flex; justify-content: center; align-items: center; height: 100vh; }
        .login-form { background-color: #fff; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); width: 300px; }
        .login-form h2 { margin-top: 0; margin-bottom: 20px; text-align: center; }
        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; font-weight: bold; }
        .form-group input { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
        button { width: 100%; padding: 10px; background-color: #007bff; color: #fff; border: none; border-radius: 5px; cursor: pointer; transition: background-color 0.3s ease; }
        button:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <div class="login-container">
        <form class="login-form" method="post">
            {% csrf_token %}
            <h2>Login</h2>
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>

```

`playground/templates/success.html`

```
<!DOCTYPE html>
<html>
<head>
    <title>Success</title>
</head>
<body>
    <h1>Login Successful</h1>
</body>
</html>

```

`playground/templates/login_error.html`

```python
<!DOCTYPE html>
<html>
<head>
    <title>Login Error</title>
</head>
<body>
    <h1>Login Failed</h1>
    <p>Incorrect username or password.</p>
</body>
</html>

```

##### Additional Information

1. Ensure you have Django installed in your virtual environment.
2. The login functionality redirects to a success page upon successful authentication and to an error page upon failure.
3. For more information, refer to the Django documentation.
