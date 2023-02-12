from django.urls import path
from . import views

urlpatterns = [
    path('', views.update, name='update'),
    # path('<str:id>', views.update, name='update'),
]
