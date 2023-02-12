from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.join, name='join'),
    path('', include("django.contrib.auth.urls")),
]
