from django.urls import path
from . import views

urlpatterns = [
    path('add_company/', views.add_company, name='add_company'),
    path('add_department/', views.add_department, name='add_department'),
    path('', views.companies_list, name='companies_list'),
    path('<int:company_id>/', views.subdivisions, name='subdivisions'),
]
