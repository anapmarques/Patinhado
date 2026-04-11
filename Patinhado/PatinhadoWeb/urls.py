from django.urls import path
from PatinhadoWeb import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register/', views.registro, name='register'),
    path('aboutus/', views.home, name='about'),
    path('list/', views.home, name='list'),
    path('give/', views.home, name='give'),
    path('contact/', views.home, name='contact'),
]