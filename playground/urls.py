from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello, name='hello'),
    path('', views.home, name='home'),  # Root URL
]
