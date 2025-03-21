from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_create),  # Default to task_list
    path('add_task/', views.task_create, name='add_task'),  # Corrected name to task_create
    path('task_list/', views.task_list, name='task_list'),
    path('task_create/', views.task_create, name='task_create'),  # Corrected name to task_create
    path('task_edit/<int:id>/', views.task_update, name='task_update'),  # Standardized parameter to id
    path('task_delete/<int:id>/', views.task_delete, name='task_delete'),  # Corrected name to task_delete
]
