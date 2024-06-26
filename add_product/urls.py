from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product_view, name='add_product'),
    path('success/', views.product_success_view, name='product_success'),
    path('edit/<int:pk>/', views.edit_product_view, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product_view, name='delete_product'),
]
