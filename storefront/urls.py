from django.contrib import admin
from django.urls import path, include

# Main URL configurations
urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('', include('playground.urls')),  # Include the playground URLs for the root path
]
