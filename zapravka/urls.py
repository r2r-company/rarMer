from django.urls import path
from zapravka.views import list_cartridges, change_status_from_telegram  # Правильний імпорт

from . import views  # Імпорт всіх view-функцій з поточного додатку

urlpatterns = [
    path('add/', views.add_cartridge, name='add_cartridge'),
    path('', views.cartridge_list, name='cartridge_list'),
    path('update_status/<int:cartridge_id>/', views.update_cartridge_status, name='update_cartridge_status'),
    path('change_cartridge_status/', views.change_cartridge_status, name='change_cartridge_status'),  # Виправлений імпорт
    path('get_departments/', views.get_departments, name='get_departments'),
    path('get_workers/', views.get_workers, name='get_workers'),
    path('list_cartridges/', list_cartridges, name='list_cartridges'),
    path('change_status_from_telegram/<int:cartridge_id>/', change_status_from_telegram,
         name='change_status_from_telegram'),
]
