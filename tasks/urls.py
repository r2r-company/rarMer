from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('my_tasks/', views.my_tasks, name='my_tasks'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:task_id>/take/', views.take_task, name='take_task'),
    path('<int:task_id>/complete/', views.complete_task, name='complete_task'),
    path('<int:task_id>/update_status/', views.task_update_status, name='task_update_status'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),  # Add this line
    path('<int:task_id>/add_comment/', views.add_comment, name='add_comment'),
    path('new_tasks/', views.new_tasks, name='new_tasks'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('assign/<int:equipment_id>/', views.assign_task, name='assign_task'),
]
