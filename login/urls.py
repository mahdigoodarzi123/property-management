from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('main_page/', views.main_page, name='main_page'),
    path('upload_file/', views.upload_file_view, name='upload_file'),
    
]
