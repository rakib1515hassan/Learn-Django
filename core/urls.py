from django.contrib import admin
from django.urls import path

from apps1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
]
