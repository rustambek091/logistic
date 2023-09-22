from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from .models import * 

# Create your views here.


class Home(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class Services(TemplateView):
    template_name = 'Services.html'
# def Services(request):
#     servis = Service.objects.all()
    # context = {
    #     'servis':servis
    # }
    # return render(request,'services.html', context)
