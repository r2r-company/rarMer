from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_list, name='user_list'),
    path('profile/<int:user_id>/', views.profile_view, name='profile_view'),
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('my_profile/', views.my_profile, name='my_profile'),
]
