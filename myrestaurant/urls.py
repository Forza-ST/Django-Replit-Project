from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_login/', views.new_login, name='new_login'),
    path('add_dish/', views.add_dish, name='add_dish'),
