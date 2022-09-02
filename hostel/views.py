from django.views.generic.list import ListView
from django.shortcuts import render
from hostel.models import *
# Create your views here.

class HomePageView(ListView):
    model = LeaveRequest
    template_name = "home.html"
    context_object_name = "book"
    login_url = "/login/"
