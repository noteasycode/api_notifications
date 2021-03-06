from django.urls import path

from . import views


app_name = 'notifications'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_notification, name='new_notification'),
    path('list/<str:username>/', views.notifications_list, name='notifications_list'),
    path('edit/<str:username>/<int:pk>/', views.edit_notification, name='edit'),
    path('delete/<str:username>/<int:pk>/', views.delete_notification, name='delete'),
]
