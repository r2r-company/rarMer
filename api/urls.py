from django.urls import path
from . import views
from zapravka.views import change_cartridge_status

urlpatterns = [
    path('notify/', views.notify, name='notify'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('departments/', views.api_departments, name='api_departments'),
    path('users/', views.api_users, name='api_users'),
    path('computer_info/', views.api_computer_info, name='api_computer_info'),
    path('live_data/', views.live_data, name='live_data'),
    path('cartridges/', views.cartridge_list_api, name='cartridge_list_api'),
    path('change_status/', change_cartridge_status, name='change_cartridge_status'),
]
