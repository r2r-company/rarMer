from django.urls import path
from . import views

urlpatterns = [
    path('', views.access_list, name='access_list'),
    path('add/', views.access_add, name='access_add'),
    path('edit/<int:pk>/', views.access_edit, name='access_edit'),
    path('delete/<int:pk>/', views.access_delete, name='access_delete'),
    path('api/departments/', views.get_departments, name='get_departments'),
    path('api/users/', views.get_users, name='get_users'),
]
