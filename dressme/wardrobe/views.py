from django.shortcuts import render
from django.views import generic

# Create your views here.

class RegisterFormView(generic.TemplateView):
    template_name = 'register.html'
