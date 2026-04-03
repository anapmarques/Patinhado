from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'PatinhadoWeb/Home.html')

def profile(request):
    return render(request, 'PatinhadoWeb/Profile.html')