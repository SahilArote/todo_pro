from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('toggle/<int:id>/', views.toggle_complete, name='toggle'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('history/<int:id>/', views.history, name='history'),
    path('history/', views.history_index, name='history_index'),      # new index
    path('accounts/local/register/', views.register, name='local_register'),
    path('accounts/local/login/', views.local_login, name='local_login'),
    path('accounts/local/logout/', views.local_logout, name='local_logout'),
    path('accounts/', include('allauth.urls')),   # allauth (social login)




]