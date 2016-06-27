from django.shortcuts import render
from django.views.generic import View

# Create your views here.

def home(request):
    title = "hello world"
    context = {
        title:"title",
    }
    return render(request, "base.html", context)
