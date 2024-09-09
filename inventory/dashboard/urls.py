from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.index, name = 'dashboard-index'),
    path('users/', views.users, name = 'dashboard-users'),
    path('inventory/', views.inventory, name = 'dashboard-inventory'),
    path('inventory/delete/<int:pk>/', views.product_delete, name = 'dashboard-product-delete'),
    path('inventory/detail/<int:pk>/', views.product_detail, name = 'dashboard-product-detail'),
    path('inventory/detail/update/<int:pk>/', views.product_update, name = 'dashboard-product-update'),
    path('orders/', views.orders, name = 'dashboard-orders'),
    path('orders/delete/<int:pk>/', views.order_delete, name = 'dashboard-order-delete'),
    path('orders/edit/<int:pk>/', views.order_edit, name = 'dashboard-order-edit'),
    path('orders/receive/<int:pk>/', views.order_received, name = 'dashboard-order-receive'),
    path('requests/', views.requests, name = 'dashboard-requests'),
    path('requests/delete/<int:pk>/', views.request_delete, name = 'dashboard-request-delete'),
    path('requests/edit/<int:pk>/', views.request_edit, name = 'dashboard-request-edit'),
    path('request/ordered/<int:pk>/', views.request_ordered, name = 'dashboard-request-order'),
    path('dashboard/delete/<int:pk>/', views.culture_delete, name = 'dashboard-culture-delete'),
    path('dashboard/edit/<int:pk>/', views.order_edit, name = 'dashboard-culture-edit'),

]
