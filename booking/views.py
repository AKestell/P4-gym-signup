from django.shortcuts import render
from django.views import generic
from .models import GymClass


# Create your views here.
class GymClassView(generic.ListView):
    queryset = GymClass.objects.all()
    template_name = "index.html"