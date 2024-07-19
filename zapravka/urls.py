from django.urls import path
from zapravka.views import change_cartridge_status

from . import views

urlpatterns = [
    path('add/', views.add_cartridge, name='add_cartridge'),
    path('', views.cartridge_list, name='cartridge_list'),
    path('update_status/<int:cartridge_id>/', views.update_cartridge_status, name='update_cartridge_status'),
    path('change_cartridge_status/', change_cartridge_status, name='change_cartridge_status'),
    path('get_departments/', views.get_departments, name='get_departments'),
    path('get_workers/', views.get_workers, name='get_workers'),

]
