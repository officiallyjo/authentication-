from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import DetailView
# Create your views here.


class CustomLoginView(LoginView):
    template_name="login.html"
    
class CustomLogoutView(LogoutView):
    template_name ="logout.html"
    
class dashboard(DetailView):
    template_name='dashboard.html'