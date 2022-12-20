from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world_func, name='hello_world')
]
