from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/list/', views.task_list, name='task_list'),
    path('task/update/<int:task_id>/', views.task_update, name='task_update'),
    path('task/delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('calendar/', views.calendar_view, name='calendar_view'),
]
