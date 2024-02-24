from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, "norbitweb/index.html")
    # return HttpResponse("Hi")

def about(request):
    return render(request, "norbitweb/about.html")

def contact(request):
    return render(request, "norbitweb/contact.html")