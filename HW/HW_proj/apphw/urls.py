
from django.urls import path
from . import views

urlpatterns = [
    path('create_client/<int:count>', views.create_client, name='create_client'),
    path('', views.login_user, name='login_user'),
    path('view_client/<int:client_id>/', views.view_client, name='view_client'),
    path('update_client/<int:client_id>/', views.update_client, name='update_client'),
    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client'),
    path('ordered_products/<int:client_id>/<str:period>/', views.ordered_products, name='ordered_products'),
    path('add_product', views.add_product, name='add_product'),
    path('products_list', views.products_list, name='products_list'),
    path('orders', views.orders, name='orders'),
    path('make_order', views.make_order, name='make_order'),
    path('client_list', views.client_list, name='client_list'),
]
