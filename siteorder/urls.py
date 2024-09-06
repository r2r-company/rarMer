from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_list, name='site_list'),
    path('add-site/', views.add_site, name='add_site'),
    path('edit-site/<int:pk>/', views.edit_site, name='edit_site'),
    path('site-detail/<int:pk>/', views.site_detail, name='site_detail'),
    path('delete-site/<int:pk>/', views.delete_site, name='delete_site'),
    path('add-payment/', views.add_payment, name='add_payment'),
    path('edit-payment/<int:pk>/', views.edit_payment, name='edit_payment'),
    path('payment-detail/<int:pk>/', views.payment_detail, name='payment_detail'),
    path('delete-payment/<int:pk>/', views.delete_payment, name='delete_payment'),
    path('add-tariff/', views.add_tariff, name='add_tariff'),
    path('edit-tariff/<int:pk>/', views.edit_tariff, name='edit_tariff'),  # Доданий шлях
    path('tariff-detail/<int:pk>/', views.tariff_detail, name='tariff_detail'),
    path('delete-tariff/<int:pk>/', views.delete_tariff, name='delete_tariff'),
    path('get-tariff-price/', views.get_tariff_price, name='get_tariff_price'),

]
