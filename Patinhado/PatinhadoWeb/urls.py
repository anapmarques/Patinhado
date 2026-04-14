from django.urls import path, reverse_lazy
from PatinhadoWeb import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(template_name="PatinhadoWeb/auth/Login.html"), name='login'),
    path('register/', views.registro, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('aboutus/', views.home, name='about'),
    path('list/', views.home, name='list'),
    path('give/', views.home, name='give'),
    path('contact/', views.home, name='contact'),
    path('pets/add/', views.PetAddView.as_view(), name='addpet'),
]