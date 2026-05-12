from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('login', include('home.urls')),
    path('signup', include('home.urls')),
    path('admission_form', include('home.urls')),
]
