from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/public/', views.public, name='public'),
    path('api/private/', views.private, name='private'),
]