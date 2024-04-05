
from django.urls import path
from . import views

urlpatterns = [
    path('create_client/', views.create_client, name='create_client'),
    path('client_list/', views.client_list, name='client_list'),
    path('view_client/<int:client_id>/', views.view_client, name='view_client'),
    path('update_client/<int:client_id>/', views.update_client, name='update_client'),
    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client'),
    path('ordered_products/<int:client_id>/<str:period>/', views.ordered_products, name='ordered_products'),
]
