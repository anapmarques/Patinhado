from django.urls import path
from PatinhadoWeb import views

urlpatterns = [
    path('', views.home),
]