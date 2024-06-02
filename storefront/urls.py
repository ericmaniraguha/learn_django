from django.contrib import admin
from django.urls import path, include
import debug_toolbar

# Main URL configurations
urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('', include('playground.urls')),  # Include the playground URLs for the root path
    path('__debug__/', include('debug_toolbar.urls')),  # Debug toolbar URL configuration
]
