# workers/urls.py
from django.urls import path
from .views import worker_list, profile_view, get_ad_users, create_profile

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('list/', worker_list, name='worker_list'),
    path('ad-users/', get_ad_users, name='ad_users'),
    path('create-profile/', create_profile, name='create_profile'),
]
