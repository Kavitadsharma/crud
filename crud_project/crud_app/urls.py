# crud_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_item, name='create_item'),
    path('list/', views.list_items, name='list_items'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item')
     
]
