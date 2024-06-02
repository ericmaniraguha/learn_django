from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.index, name='login'),  # view for the login page
    path('success/', views.success, name='success'),  # view for the success page
    path('login_error/', views.login_error, name='login_error'),  # Login error page
    # Add other paths as needed
]