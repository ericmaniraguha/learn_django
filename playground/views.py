from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
    # Ensure the default user exists
    if not User.objects.filter(username='ericmaniraguha').exists():
        User.objects.create_user(username='ericmaniraguha', password='password')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success')  # Replace 'success' with your desired success URL
        else:
            return redirect('login_error')  # Redirect to the error page
    return render(request, 'index.html')

def login_error(request):
    return render(request, 'login_error.html')

def success(request):
    return render(request, 'success.html')
