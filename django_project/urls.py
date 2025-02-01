from django.urls import path
from myrestaurant import views
from django.contrib import admin
urlpatterns =[ 
    path('admin/', admin.site.urls),  # Default admin URL path
    path('', views.index, name='index'),
    path('new_login/', views.new_login, name='new_login'),
    path('add_dish/', views.add_dish, name='add_dish'),
]