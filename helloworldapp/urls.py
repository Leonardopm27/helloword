from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld_views, name='helloworld_views'),
]