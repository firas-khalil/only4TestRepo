from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('list', views.list, name="list"),
    path('updateTask/<str:pk>/', views.updateTask, name="updateTask"),
    path('deleteTask/<str:pk>/', views.deleteTask, name="deleteTask"),
]
